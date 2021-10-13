from pkg.decorators import setup_file_required
from utils import CapturingOutput
from test_commands import HERE
import unittest


class DecoratorTest(unittest.TestCase):
    def test_setup_file_required(self):
        func = setup_file_required(lambda: print('Function Done!'))

        with CapturingOutput() as output:
            (HERE / 'setup.cfg').touch(exist_ok=True)
            func()
            (HERE / 'setup.cfg').unlink(missing_ok=True)
            func()

        self.assertEqual(output[0], 'Function Done!')
        self.assertEqual(output[1], 'Error: The "setup.cfg" file is required!!')


if __name__ == '__main__':
    unittest.main()
