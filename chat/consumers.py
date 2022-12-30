from datetime import datetime
from uuid import uuid4

from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models import Chatter, Chat


class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'anonymous_chat'

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
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
            data = content.get('ip', None)
            if not data:
                return
            else:
                chatter = await Chatter.objects.acreate(
                    hashed_value=str(uuid4())[:8],
                    ip_address=data.get('query', None),
                    country=data.get('country', None),
                    region_name=data.get('regionName', None),
                    city=data.get('city', None),
                    timezone=data.get('timezone', None)
                )
                await self.send_json({'success': True, 'chatter_id': chatter.id, 'hashed_value': chatter.hashed_value})

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
