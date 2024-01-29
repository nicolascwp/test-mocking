from othermodule import ClassToMock


class ModuleClass:
    def __init__(self):
        self.class_to_mock = ClassToMock()

    def get_from_init(self):
        return self.class_to_mock.out()

    def get_from_local_import(self):
        from othermodule import ClassToMock
        return ClassToMock().out()
