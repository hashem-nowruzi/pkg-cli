from .commands import InitCommand
import sys


class PKG:
    def __init__(self, argv):
        self.argv = argv if argv else None

    def execute(self) -> None:
        if self.argv is None:
            return

        command = self.argv[0]
        if command == 'init':
            InitCommand(self.argv[1:]).execute()


def main():
    pkg = PKG(sys.argv[1:])
    pkg.execute()


if __name__ == '__main__':
    main()
