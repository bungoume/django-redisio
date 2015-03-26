from django.test import TestCase
from django.test.utils import override_settings


class TestCheckRequiredSettings(TestCase):
    def _callFUT(self, *args, **kwargs):
        from redisio.checks import check_required_settings
        return check_required_settings(*args, **kwargs)

    @override_settings(
        REDISIO_CLIENT_CLASS=None,
        REDISIO_HOST=None,
        REDISIO_PORT=None,
        REDISIO_DB=None,
    )
    def test__errors(self):
        actual = self._callFUT('dummy app_configs')

        self.assertEqual(len(actual), 4)
        self.assertEqual(actual[0].msg,
                         "'REDISIO_CLIENT_CLASS' setting is required in settings file")
        self.assertEqual(actual[1].msg,
                         "'REDISIO_HOST' setting is required in settings file")
        self.assertEqual(actual[2].msg,
                         "'REDISIO_PORT' setting is required in settings file")
        self.assertEqual(actual[3].msg,
                         "'REDISIO_DB' settings is required in settings file")

    @override_settings(
        REDISIO_CLIENT_CLASS='client class',
        REDISIO_HOST='host',
        REDISIO_PORT='port',
        REDISIO_DB='db',
    )
    def test__no_errors(self):
        actual = self._callFUT('dummy app_configs')
        self.assertEqual(actual, [])
