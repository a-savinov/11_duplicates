import argparse
import os
from collections import namedtuple, defaultdict


def find_file_duplicates(path_to_dir):
    dict_of_files = defaultdict(list)
    file_info = namedtuple('Fileinfo', ['name', 'size'])
    for dir_path, sub_dirs, file_names in os.walk(path_to_dir):
        for file_name in file_names:
            file_size = os.stat(os.path.join(dir_path, file_name)).st_size
            file_path = os.path.join(dir_path, file_name)
            file_params = file_info(file_name, file_size)
            if not dict_of_files.get(file_params):
                dict_of_files.update({file_params: [file_path]})
            else:
                duplicates_path_list = dict_of_files.get(file_params)
                duplicates_path_list.append(file_path)
                dict_of_files.update(
                    {file_params: duplicates_path_list})
    return dict_of_files


def print_file_duplicates(dict_files):
    for file_info, files_paths in dict_files.items():
        if len(files_paths) > 1:
            print('File name: {}  File size: {} - Duplicates list: {}'.format(
                file_info.name, file_info.size, files_paths))


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', required=True,
                        help='Path to DIR for analyse')
    return parser


if __name__ == '__main__':
    parser = get_input_argument_parser()
    args = parser.parse_args()
    path_to_dir = args.dir
    dict_files = find_file_duplicates(path_to_dir)
    print_file_duplicates(dict_files)
