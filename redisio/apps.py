from django.apps import AppConfig
from django.core import checks

from redisio.checks import check_required_settings


class RedisioConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""

    name = 'redisio'
    verbose_name = "Redis utility for django"

    def ready(self):
        checks.register('settings')(check_required_settings)
