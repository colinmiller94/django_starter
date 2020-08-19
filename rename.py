"""Rename Django Project. May need to add some sql to fix database"""


import argparse
import os

DEFAULT_NAME = 'django_project'
BLACKLIST_DIRS = ['.git', 'migrations', '__pycache__', '.idea']
BLACKLIST_FILES = ['.DS_Store', 'db.sqlite3']

THIS_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# helper function
def skip(string, skip_list):
    # truthy if one of the elements in the skip_list is in string
    return sum([s in string for s in skip_list])


def rename(directory, old, new):
    """
    Find/replace and rename directories/files.

    :param str directory: Directory to conduct find/replace in
    :param str old: old name
    :param str new: new name
    :return:
    """
    for root, dirs, files in os.walk(directory, topdown=False):
        if skip(root, BLACKLIST_DIRS):
            continue

        # Alter files first
        for file in files:
            if skip(file, BLACKLIST_FILES):
                continue
            full_old_path = os.path.join(root, file)
            full_new_path = os.path.join(root, file.replace(old, new))
            with open(full_old_path, 'r', encoding='utf-8') as f:
                text = f.read().replace(old, new)

            with open(full_new_path, 'w+', encoding='utf-8') as f:
                f.write(text)

        # only alter tail of root path
        head, tail = os.path.split(root)
        new_root = os.path.join(head, tail.replace(old, new))
        os.rename(root, new_root)


def main():
    parser = argparse.ArgumentParser(
        description='Rename the protect. Renames files and replaces references in files'
    )

    parser.add_argument('-o', '--old', action='store', type=str, default=DEFAULT_NAME,
                        help=f'Specify old name with --old=old Default: {DEFAULT_NAME}', dest='old')

    parser.add_argument('-n', '--new', action='store', type=str, default=DEFAULT_NAME,
                        help=f'Specify new name with --new=new Default: {DEFAULT_NAME}', dest='new')

    parser.add_argument('-d', '--directory', action='store', type=str, default=THIS_DIR,
                        help=f'Specify directory to alter with --directory=directory Default: {THIS_DIR}',
                        dest='directory')

    args = parser.parse_args()
    rename(directory=args.directory, old=args.old, new=args.new)


if __name__ == '__main__':
    main()
