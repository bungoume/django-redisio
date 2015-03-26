from django.conf import settings
from django.core.checks import Error


def check_required_settings(app_configs, **kwargs):
    """ Checking required settigs.
    """
    msgs = []
    # Use getattr(...) is None for testing instead of hasattr.
    # Cause override_settings cant delete attributes on settings.
    if getattr(settings, 'REDISIO_CLIENT_CLASS', None) is None:
        msgs.append(
            Error("'REDISIO_CLIENT_CLASS' setting is required in settings file")
        )

    if getattr(settings, 'REDISIO_HOST', None) is None:
        msgs.append(
            Error("'REDISIO_HOST' setting is required in settings file")
        )

    if getattr(settings, 'REDISIO_PORT', None) is None:
        msgs.append(
            Error("'REDISIO_PORT' setting is required in settings file")
        )

    if getattr(settings, 'REDISIO_DB', None) is None:
        msgs.append(
            Error("'REDISIO_DB' settings is required in settings file")
        )

    return msgs
