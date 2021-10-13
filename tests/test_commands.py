import unittest
from pkg.__main__ import get_parser
from pathlib import Path

HERE = Path(__file__).parent


class BaseCommandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = get_parser()

    def tearDown(self) -> None:
        (HERE / 'setup.cfg').unlink(missing_ok=True)


class InitCommandTest(BaseCommandTest):
    def test_package_json(self):
        args = self.parser.parse_args(['init'])
        args.func(args)

        self.assertTrue((HERE / 'setup.cfg').is_file())


if __name__ == '__main__':
    unittest.main()
