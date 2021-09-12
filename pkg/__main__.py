import sys


class PKG:
    def __init__(self, argv):
        self.argv = argv if argv else None

    def execute(self) -> None:
        if self.argv is None:
            return
        pass


def main():
    pkg = PKG(sys.argv[1:])
    pkg.execute()


if __name__ == '__main__':
    main()
