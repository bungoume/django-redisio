from importlib import import_module

from django.conf import settings


def _import_by_path(path):
    """ Import functions or classes by module path string.

    >>> _import_by_path('redis.StrictRedis')
    <class 'redis.client.StrictRedis'>
    """
    module_path, attr_name = path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, attr_name)


def get_client():
    """ Create client object for redis from settings.
    """
    client_class = _import_by_path(settings.REDISIO_CLIENT_CLASS)
    return client_class(host=settings.REDISIO_HOST,
                        port=settings.REDISIO_PORT,
                        db=settings.REDISIO_DB)
