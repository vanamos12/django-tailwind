from django.apps import AppConfig


class AuthenConfig(AppConfig):
    name = 'authen'

    def ready(self) -> None:
        import authen.signals