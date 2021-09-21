import unittest
from pkg.__main__ import PKG


class BaseCommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = PKG().parser


if __name__ == '__main__':
    unittest.main()
