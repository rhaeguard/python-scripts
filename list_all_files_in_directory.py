import os

def get_all_file_full_paths_in_sub_directories(root):
    return [os.path.join(path, file) for path, _, files in os.walk(root) for file in files]

def get_all_file_names_in_sub_directories(root):
    return [file for _, _, files in os.walk(root) for file in files]

def get_all_file_names_in_sub_directories_with_filter(root, filterFunc):
    return filter(filterFunc, get_all_file_names_in_sub_directories(root))