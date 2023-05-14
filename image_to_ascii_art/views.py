from asgiref.sync import sync_to_async
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpRequest
from django.shortcuts import render

from home.views import BaseFormView
from image_to_ascii_art.forms import ImageUploadForm, UserUploadedImageForm
from image_to_ascii_art.tasks import draw_ascii_art


class ImageToAsciiView(BaseFormView):
    template_name = "image_to_ascii_art/main.html"
    form_class = ImageUploadForm
    view_is_async = True

    async def get(self, request: HttpRequest, *args, **kwargs):
        context = await sync_to_async(self.get_context_data)(**kwargs)
        return self.render_to_response(context)

    @sync_to_async
    def get_user_from_request(self, request: HttpRequest) -> User | AnonymousUser | None:
        return request.user if bool(request.user) else None

    async def post(self, request: HttpRequest, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        user = await self.get_user_from_request(request)

        if user:
            data = dict(request.POST)
            data['user'] = request.user
            data['image'] = request.FILES.get('image', None)
            compress_amount = data.pop('compress_amount')
            data.pop('csrfmiddlewaretoken')

            new_form = UserUploadedImageForm(data, request.FILES)

            is_valid = await sync_to_async(new_form.is_valid)()

            if is_valid:
                instance = await sync_to_async(new_form.save)()
                draw_ascii_art.delay(pk=instance.pk, compress_amount=int(compress_amount[0]))
                return render(request, 'image_to_ascii_art/result_success.html', {})

        return self.form_invalid(form)
