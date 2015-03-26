from django.test import TestCase


class TestImportByPath(TestCase):
    def _getTarget(self):
        from redisio.client import _import_by_path
        return _import_by_path

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__import(self):
        target = self._getTarget()
        actual = target('redisio.client._import_by_path')
        self.assertEqual(actual, target)

    def test__import_error(self):
        with self.assertRaises(ImportError):
            self._callFUT('notexistedmodule._import_by_path')

    def test__attribute_error(self):
        with self.assertRaises(AttributeError):
            self._callFUT('redisio.client.notexistedattribute')
