import os
import sys


def find_file_duplicates(path_to_dir):
    dict_of_files = {}
    dict_of_duplicates = {}
    for dirpath, subdirs, filenames in os.walk(path_to_dir):
        for file in filenames:
            file_size = os.stat(os.path.join(dirpath, file)).st_size
            file_path = os.path.join(dirpath, file)
            if dict_of_files.get(file) == None:
                dict_of_files.update({file: file_size})
            elif dict_of_files.get(file) == file_size:
                dict_of_duplicates.update({file_path: file_size})
            else:
                pass
    return dict_of_duplicates


def print_file_duplicates(files_dict):
    for file in files_dict.keys():
        print('Duplicate: ' + file + ' file size: ' + str(files_dict.get(file)))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path_to_dir = sys.argv[1]
        files_dict = find_file_duplicates(path_to_dir)
        print_file_duplicates(files_dict)
    else:
        print('Please define path to dir for analyse \nExample: python duplicates.py <path_to_dir>')
