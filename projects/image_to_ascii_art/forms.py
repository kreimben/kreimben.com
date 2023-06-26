from django import forms

from projects.image_to_ascii_art.models import UserUploadedImage


class ImageUploadForm(forms.ModelForm):
    """
    Just for get compression level.
    """
    compress_amount = forms.IntegerField(min_value=1, max_value=10, initial=3)
    is_public = forms.BooleanField(required=True, initial=True)

    class Meta:
        model = UserUploadedImage
        fields = ['image']


class UserUploadedImageForm(forms.ModelForm):
    """
    It's for save image with user.
    """

    class Meta:
        model = UserUploadedImage
        fields = ['user', 'image']


class MakeThisImagePublicForm(forms.Form):
    """
    It's for make image public or private.
    """
    make_public = forms.BooleanField(required=False, initial=True)


class DeleteConvertingResult(forms.Form):
    """
    It's for delete converting result.
    """
    pk = forms.IntegerField(required=True)  # ImageConvertingResult pk
