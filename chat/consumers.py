from datetime import datetime
from uuid import uuid4

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

from chat.models import Chatter, Chat


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'anonymous_chat'
        self.chatter = None

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.broadcast',
                'message': f'{self.chatter.hashed_value if self.chatter is not None else ""} has left.',
                'hashed_value': '[System]',
                'chatter_id': self.chatter.id if self.chatter is not None else 0
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        print(f'{content=}')
        if content.get('message', None):
            chat = await Chat.objects.acreate(message=content.get('message', None),
                                              chatter_id=content.get('chatter_id', None))

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.broadcast",
                    "message": chat.message,
                    'hashed_value': content.get('hashed_value', None),
                    'chatter_id': chat.chatter_id
                }
            )
        elif content.get('ip', None):
            ip_address = content.get('ip', None)
            g = GeoIP2()
            try:
                location = g.city(ip_address)

                self.chatter = await Chatter.objects.acreate(
                    hashed_value=str(uuid4())[:8],
                    ip_address=ip_address,
                    country=location["country_name"],
                    region_name=location['region'],
                    city=location["city"],
                    timezone=location['time_zone']
                )
                print(f'{self.chatter=}')
                await self.send_json(
                    {'success': True, 'chatter_id': self.chatter.id, 'hashed_value': self.chatter.hashed_value})
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat.broadcast',
                        'message': f'{self.chatter.hashed_value} has entered.',
                        'hashed_value': 'System',
                        'chatter_id': self.chatter.id
                    }
                )
            except AddressNotFoundError as _:
                await self.send_json({
                    'success': False,
                    'msg': 'Failed to get geo info.'
                })

    async def chat_broadcast(self, event):
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = event.get('message', None)
        hashed_value = event.get('hashed_value', None)
        chatter_id = event.get('chatter_id', None)

        await self.send_json({
            'message': message,
            'hashed_value': hashed_value,
            'chatter_id': chatter_id,
            'time': time
        })
