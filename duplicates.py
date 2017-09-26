import os
import sys


def find_file_duplicates(path_to_dir):
    dict_of_orig_files = {}
    list_of_duplicates = []
    for dirpath, subdirs, filenames in os.walk(path_to_dir):
        for file in filenames:
            file_size = os.stat(os.path.join(dirpath, file)).st_size
            file_path = os.path.join(dirpath, file)
            if dict_of_orig_files.get((file, file_size,)) == None:
                dict_of_orig_files.update({(file, file_size,): file_path})
            else:
                list_of_duplicates.append((file, file_size, file_path))
    return dict_of_orig_files, list_of_duplicates


def print_file_duplicates(files_list):
    for file in files_list:
        print('Original file: ' + dict_of_orig_files.get((file[0], file[1],)))
        print('\tDuplicate: ' + file[2] + ' file size: ' + str(file[1]))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_dir = sys.argv[1]
        dict_of_orig_files, list_of_duplicates = find_file_duplicates(path_to_dir)
        print_file_duplicates(list_of_duplicates)
    else:
        print('Please define path to dir for analyse \nExample: python duplicates.py <path_to_dir>')
