import subprocess
import sys


def python(*args):
    command = [sys.executable]
    command.extend(args)
    subprocess.run(command)
