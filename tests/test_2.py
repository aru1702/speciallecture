import unittest


def set_up_module():
    print("Running setUpModule")


def tear_down_module():
    print("Running tearDownModule")


class TestTwo(unittest.TestCase):
    @classmethod
    def set_up_class(cls):
        print("Running setUpClass")

    @classmethod
    def tear_down_class(cls):
        print("Running tearDownClass")

    def set_up(self):
        print("Running setUp")

    def tear_down(self):
        print("Running tearDown")

    def test_read1(self):
        print("Running test_read1")

    def test_read2(self):
        print("Running test_read2")
