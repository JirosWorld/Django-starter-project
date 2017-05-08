from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = '{{ project_name|lower }}.utils'

    def ready(self):
        from . import checks  # noqa
