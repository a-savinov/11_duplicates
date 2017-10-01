import os
import sys


def find_file_duplicates(path_to_dir):
    dict_of_orig_files = {}
    list_of_duplicates = []
    for dir_path, sub_dirs, file_names in os.walk(path_to_dir):
        for file_name in file_names:
            file_size = os.stat(os.path.join(dir_path, file_name)).st_size
            file_path = os.path.join(dir_path, file_name)
            if dict_of_orig_files.get((file_name, file_size,)) is None:
                dict_of_orig_files.update({(file_name, file_size,): file_path})
            else:
                list_of_duplicates.append((file_name, file_size, file_path))
    return dict_of_orig_files, list_of_duplicates


def print_file_duplicates(files_list):
    for file in files_list:
        print('Duplicate: {}  file size: {} - Original file: {} '.format(file[2],
                                                                         file[1],
                                                                         dict_orig_files.get((file[0], file[1],))))


if __name__ == '__main__':
    if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
        path_to_dir = sys.argv[1]
        dict_orig_files, list_duplicates = find_file_duplicates(path_to_dir)
        print_file_duplicates(list_duplicates)
    else:
        print('Please define path to dir for analyse \nExample: python duplicates.py <path_to_dir>')
