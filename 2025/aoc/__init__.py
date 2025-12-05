import os
import sys


def get_input():
    """Returns a list of strings via readlines()"""

    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    filepath = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), filename)

    if not os.path.exists(filepath):
        sys.stderr.write(f"File does not exist: {filepath}")
        sys.exit(1)

    with open(filepath, "r") as f:
        return f.readlines()
