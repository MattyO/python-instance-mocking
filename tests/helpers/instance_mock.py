from unittest import mock

class InstanceMock():
    instances = []

    def __call__(self, *args, **kwargs):
        self.instances.append(mock.MagicMock())
        return self.instances[-1]

    @classmethod
    def last_instance(cls):
        return cls.instances[-1]

def create_mock(*args, **kwargs):
    InstanceMock.instances.clear()
    return InstanceMock()

