from django.apps import AppConfig


class DjangoAppConfig(AppConfig):
    name = 'django_app'

    def ready(self):
        import django_app.signals
