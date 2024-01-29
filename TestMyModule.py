import unittest
from unittest.mock import patch

from mymodule import ModuleClass


class MyTestCase(unittest.TestCase):

    # Passes
    @patch('othermodule.ClassToMock')
    def test_othermodule_ClassToMock_get_from_local_import(self, mocked_class):
        mocked_class.return_value.out.return_value = 'mocked'
        module_class = ModuleClass()
        self.assertEqual(module_class.get_from_local_import(), 'mocked', 'get_from_local_import')

    # Fails: the test uses the un-patched ClassToMock
    @patch('othermodule.ClassToMock')
    def test_othermodule_ClassToMock_get_from_init(self, mocked_class):
        mocked_class.return_value.out.return_value = 'mocked'
        module_class = ModuleClass()
        self.assertEqual(module_class.get_from_init(), 'mocked', 'get_from_init')

    # AttributeError: <class 'othermodule.ClassToMock.ClassToMock'> does not have the attribute 'ClassToMock'
    @patch('othermodule.ClassToMock.ClassToMock')
    def test_othermodule_ClassToMock_ClassToMock(self, mocked_class):
        mocked_class.return_value.out.return_value = 'mocked'
        module_class = ModuleClass()
        self.assertEqual(module_class.get_from_init(), module_class.get_from_local_import(), 'out1 == out2')
        self.assertEqual(module_class.get_from_local_import(), 'mocked', 'get_from_local_import')
        self.assertEqual(module_class.get_from_init(), 'mocked', 'get_from_init')

    # AttributeError: <class 'mymodule.ModuleClass.ModuleClass'> does not have the attribute 'ClassToMock'
    @patch('mymodule.ModuleClass.ClassToMock')
    def test_mymodule_ModuleClass_ClassToMock(self, mocked_class):
        mocked_class.return_value.out.return_value = 'mocked'
        module_class = ModuleClass()
        self.assertEqual(module_class.get_from_init(), module_class.get_from_local_import(), 'out1 == out2')
        self.assertEqual(module_class.get_from_local_import(), 'mocked', 'get_from_init')
        self.assertEqual(module_class.get_from_init(), 'mocked', 'get_from_init')

    @patch('mymodule.ClassToMock')  # Fails get_from_local_import get_from_init
    def test_mymodule_ClassToMock(self, mocked_class):
        mocked_class.return_value.out.return_value = 'mocked'
        module_class = ModuleClass()
        self.assertEqual(module_class.get_from_init(), module_class.get_from_local_import(), 'out1 == out2')
        self.assertEqual(module_class.get_from_local_import(), 'mocked', 'get_from_local_import')
        self.assertEqual(module_class.get_from_init(), 'mocked', 'get_from_init')


if __name__ == '__main__':
    unittest.main()
