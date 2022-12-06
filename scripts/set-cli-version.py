import os
import re
import sys
import traceback
import argparse

def main(file):
    try:
        path_file = os.path.join(os.getcwd(), file)
        tmp_path_file = f'{path_file}.tmp'
        regex = '^\s?version.*$'
        with open(path_file, 'r') as read_file:
            with open(tmp_path_file, 'w') as write_file:
                lines = read_file.read()
                new_lines = re.sub(regex, f"version = \"{os.getenv('GITVERSION_MAJORMINORPATCH')}\"", lines, flags=re.MULTILINE)
                write_file.write(new_lines)
            os.remove(path_file)
            os.rename(tmp_path_file, path_file)
    except:
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='.')
    parser.add_argument("-f", "--file", help="Pyproject.toml to process")
    args = parser.parse_args()
    main(args.file)