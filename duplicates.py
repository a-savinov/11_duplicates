import argparse
import os


def find_file_duplicates(path_to_dir):
    dict_of_files = {}
    for dir_path, sub_dirs, file_names in os.walk(path_to_dir):
        for file_name in file_names:
            file_size = os.stat(os.path.join(dir_path, file_name)).st_size
            file_path = os.path.join(dir_path, file_name)
            if dict_of_files.get((file_name, file_size,)) is None:
                dict_of_files.update({(file_name, file_size,): [file_path]})
            else:
                duplicates_path_list = dict_of_files.get(
                    (file_name, file_size,))
                duplicates_path_list.append(file_path)
                dict_of_files.update(
                    {(file_name, file_size,): duplicates_path_list})
    return dict_of_files


def print_file_duplicates(dict_files):
    for file_key, file_value in dict_files.items():
        if len(file_value) > 1:
            print('File name: {}  File size: {} - Duplicates list: {}'.format(
                file_key[0], file_key[1], file_value))


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', required=True,
                        help='Path to DIR for analyse')
    return parser


if __name__ == '__main__':
    parser = get_input_argument_parser()
    namespace = parser.parse_args()
    path_to_dir = namespace.dir
    dict_files = find_file_duplicates(path_to_dir)
    print_file_duplicates(dict_files)
