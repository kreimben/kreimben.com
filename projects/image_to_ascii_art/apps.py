from django.apps import AppConfig


class ImageToAsciiArtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projects.image_to_ascii_art'

    def ready(self):
        from projects.image_to_ascii_art import signals
        signals.load()
