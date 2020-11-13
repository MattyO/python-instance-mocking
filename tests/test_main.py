import unittest
from unittest import mock

import main

class InstanceMockTest(unittest.TestCase):

    @mock.patch("instance.Instance")
    def test_instance_mock(self, class_mock):
        every_instance = class_mock.return_value
        self.assertEqual(
            main.Thing().baz(),
            every_instance.bar.return_value
        )



