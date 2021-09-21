import unittest
from pkg.__main__ import PKG
from pathlib import Path

HERE = Path(__file__).parent


class BaseCommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = PKG().parser

    def tearDown(self) -> None:
        (HERE / 'package.json').unlink(missing_ok=True)


class InitCommandTest(BaseCommandTest):
    def test_package_json(self):
        args = self.parser.parse_args(['init'])
        args.func(args)

        self.assertTrue((HERE / 'package.json').is_file())


if __name__ == '__main__':
    unittest.main()
