from pkg.decorators import package_json_file_required
from utils import CapturingOutput
from test_commands import HERE
import unittest


class DecoratorTest(unittest.TestCase):
    def test_package_json_file_required(self):
        func = package_json_file_required(lambda: print('Function Done!'))

        with CapturingOutput() as output:
            (HERE / 'package.json').touch(exist_ok=True)
            func()
            (HERE / 'package.json').unlink(missing_ok=True)
            func()

        self.assertEqual(output[0], 'Function Done!')
        self.assertEqual(output[1], 'Error: The "package.json" file is required!!')


if __name__ == '__main__':
    unittest.main()
