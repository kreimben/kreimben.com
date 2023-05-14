from asgiref.sync import sync_to_async
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpRequest
from django.urls import reverse

from home.views import BaseFormView, BaseTemplateView, BaseDetailView
from image_to_ascii_art.forms import ImageUploadForm, UserUploadedImageForm
from image_to_ascii_art.models import ImageConvertingResult
from image_to_ascii_art.tasks import draw_ascii_art


@sync_to_async
def get_user_from_request(request: HttpRequest) -> User | AnonymousUser | None:
    return request.user if bool(request.user) else None


class ImageToAsciiView(BaseFormView):
    template_name = "image_to_ascii_art/main.html"
    form_class = ImageUploadForm
    view_is_async = True

    def get_success_url(self):
        return reverse('image_to_ascii_art_view')

    async def get(self, request: HttpRequest, *args, **kwargs):
        context = await sync_to_async(self.get_context_data)(**kwargs)
        return self.render_to_response(context)

    async def post(self, request: HttpRequest, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        user = await get_user_from_request(request)

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
                messages.success(request, 'Image is being converted to ASCII art now.')
                return self.form_valid(form)

        return self.form_invalid(form)


class ImageConvertingResultView(BaseTemplateView):
    template_name = "image_to_ascii_art/converting_result.html"

    async def get(self, request: HttpRequest, *args, **kwargs):
        context = await sync_to_async(self.get_context_data)(**kwargs)
        user = await get_user_from_request(request)
        results = await sync_to_async(list)(
            ImageConvertingResult.objects.select_related('upload_image') \
                .filter(upload_image__user_id__exact=user.id) \
                .order_by('-created_at'))
        context['results'] = results
        return self.render_to_response(context)


class ImageConvertingResultDetailView(BaseDetailView):
    template_name = "image_to_ascii_art/converting_result_detail.html"

    async def get(self, request: HttpRequest, *args, **kwargs):
        context = await sync_to_async(self.get_context_data)(**kwargs)
        result: ImageConvertingResult = await ImageConvertingResult.objects \
            .select_related('upload_image') \
            .aget(pk=kwargs['pk'])
        print(f'{result.upload_image.image.url=}')
        context['result'] = result
        print(f'{result=}')
        return self.render_to_response(context)
