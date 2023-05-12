from django import forms

from image_to_ascii_art.models import UserUploadedImage


class ImageUploadForm(forms.ModelForm):
    """
    Just for get compression level.
    """
    compress_amount = forms.IntegerField(min_value=1, max_value=10, initial=3)

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
