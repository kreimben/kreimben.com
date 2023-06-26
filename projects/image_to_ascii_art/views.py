from asgiref.sync import sync_to_async
from django.contrib import messages
from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse

from home.views import BaseFormView
from projects.image_to_ascii_art.forms import ImageUploadForm, UserUploadedImageForm, MakeThisImagePublicForm, \
    DeleteConvertingResult
from projects.image_to_ascii_art.models import ImageConvertingResult
from projects.image_to_ascii_art.tasks import draw_ascii_art


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
            compress_amount = int(data.pop('compress_amount')[0])
            is_public = bool(data.pop('is_public')[0])
            data.pop('csrfmiddlewaretoken')

            new_form = UserUploadedImageForm(data, request.FILES)

            is_valid = await sync_to_async(new_form.is_valid)()

            if is_valid:
                instance = await sync_to_async(new_form.save)()
                _ = draw_ascii_art.delay(
                    pk=instance.pk,
                    compress_amount=compress_amount,
                    is_public=is_public
                )
                messages.success(request, 'Image is being converted to ASCII art now.')
                return self.form_valid(form)

        return self.form_invalid(form)


class ImageConvertingResultView(BaseFormView):
    template_name = "image_to_ascii_art/converting_result.html"
    form_class = DeleteConvertingResult

    def get(self, request: HttpRequest, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        results = ImageConvertingResult.objects.select_related('upload_image') \
            .filter(upload_image__user_id__exact=request.user.id) \
            .order_by('-created_at')
        context['results'] = results
        return self.render_to_response(context)

    def get_success_url(self):
        return reverse('converting_result')

    def post(self, request: HttpRequest, *args, **kwargs):
        form = DeleteConvertingResult(request.POST)
        pk = form.data.get('pk', None)
        if not pk:
            messages.error(request, 'Invalid form.')
            return self.form_invalid(form)

        if request.user.is_authenticated:
            result = ImageConvertingResult.objects \
                .select_related('upload_image') \
                .get(pk=pk)

            if result.upload_image.user == request.user:
                result.delete()
                messages.success(request, 'Ascii art is deleted.')
                return self.form_valid(form)
            else:
                messages.error(request, 'You are not owner of this image.')
                return self.form_invalid(form)
        else:
            messages.error(request, 'You are not authenticated.')
            return self.form_invalid(form)


class ImageConvertingResultDetailView(BaseFormView):
    template_name = "image_to_ascii_art/converting_result_detail.html"
    form_class = MakeThisImagePublicForm

    def get(self, request: HttpRequest, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        result = ImageConvertingResult.objects \
            .select_related('upload_image') \
            .get(pk=kwargs['pk'])

        if result.is_public or result.upload_image.user == request.user:
            context['result'] = result
            return self.render_to_response(context)
        else:
            messages.error(request, 'This image is not public.')
            return redirect(reverse('image_to_ascii_art_view'))

    def get_success_url(self):
        return reverse('image_to_ascii_art_view')

    def post(self, request: HttpRequest, *args, **kwargs):
        form = MakeThisImagePublicForm(request.POST)

        if request.user.is_authenticated:
            make_public = bool(form.data.get('make_public', False))
            result = ImageConvertingResult.objects \
                .select_related('upload_image') \
                .get(pk=kwargs['pk'])

            if result.upload_image.user == request.user:
                result.is_public = make_public
                result.save()
                if make_public is True:
                    messages.success(request, 'Image is now public.')
                else:
                    messages.success(request, 'Image is now private.')
                return self.form_valid(form)
            else:
                messages.error(request, 'You are not owner of this image.')
                return self.form_invalid(form)
        else:
            messages.error(request, 'You are not authenticated. Please log in.')
            return self.form_invalid(form)
