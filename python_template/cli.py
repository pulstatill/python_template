"""Console script for python_template."""
import argparse
import sys


def main():
    """Console script for python_template."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Test")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
