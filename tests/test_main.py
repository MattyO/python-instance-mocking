import unittest
from unittest import mock

import tests.helpers.instance_mock

import main

class InstanceMockTest(unittest.TestCase):

    @mock.patch("instance.Instance", new_callable=tests.helpers.instance_mock.create_mock)
    def test_instance_mock(self, instance_mock):
        self.assertEqual(
            main.Thing().baz(),
            instance_mock.last_instance().bar.return_value
        )

    @mock.patch("instance.Instance", new_callable=tests.helpers.instance_mock.create_mock)
    def test_instance_mock_saves_instances(self, instance_mock):
        main.Thing().baz()
        self.assertEqual(len(instance_mock.instances), 2)

    @mock.patch("instance.Instance", new_callable=tests.helpers.instance_mock.create_mock)
    def test_instance_mock_assert_not_called(self, instance_mock):
        main.Thing().baz()
        instance_mock.instances[0].bar.assert_not_called()

        instance_mock.last_instance().bar.assert_called()
        instance_mock.last_instance().zed.assert_called()


