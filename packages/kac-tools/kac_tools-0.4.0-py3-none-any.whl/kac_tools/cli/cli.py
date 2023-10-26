"""CLI Tool that distributes subcommands"""
import argparse
from kac_tools.changelog import Changelog


def parse_changelog(args):
    """Builds Changelog model from provided file and prints requested section."""
    changelog = Changelog(args.changelog_file)
    print(changelog[args.section])


def main():
    """Parses command line arguments and calls corresponding subcommand program."""
    # Bus agnostic options
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-c",
        "--changelog-file",
        default="CHANGELOG.md",
        help="Path to changelog file to parse (default: %(default)s).",
    )

    parser.add_argument(
        "-s",
        "--section",
        default="latest",
        help="Section that should be extracted (default: %(default)s).",
    )

    parser.set_defaults(func=parse_changelog)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
