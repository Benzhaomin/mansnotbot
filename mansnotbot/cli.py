# -*- coding: utf-8 -*-
import argparse
import sys
import logging


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', action='count', default=0)

    return vars(parser.parse_args(argv))


def setup_logging(verbosity):
    if verbosity >= 2:
        loglevel = logging.DEBUG
    elif verbosity == 1:
        loglevel = logging.INFO
    else:
        loglevel = logging.WARNING

    logging.basicConfig(level=loglevel, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def main():
    args = parse_args(sys.argv[1:])
    setup_logging(args.get('verbose'))

    try:
        print("Nothing yet")
    except IndexError:
        print("Please provide a command name")


if __name__ == "__main__":
    main()
