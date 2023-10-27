import os
import shutil

import pandas as pd


def select_option(obj: [list, tuple, dict, pd.DataFrame], item_name='item', key=False, extra_options: dict = None):
    if not extra_options:
        extra_options = {}

    if isinstance(obj, pd.DataFrame) and obj.shape[1] == 1:
        if key:
            return obj.columns[0]
        else:
            return obj[obj.columns[0]]
    elif isinstance(obj, dict) and len(obj) == 1:
        if key:
            return list(obj.keys())[0]
        else:
            return obj[list(obj.keys())[0]]

    elif len(obj) + len(extra_options) == 1:
        return obj[0]
    elif len(obj) == 0:
        return False

    items = {}
    for n, item in enumerate(obj):
        print(f"{n + 1}: {item}")
        items[n + 1] = item

    for option, result in extra_options.items():
        n += 1
        print(f"{n + 1}: {option}")
        items[n + 1] = result

    selection = 0
    while selection not in items:
        selection = int(input(f"Enter {item_name} number: "))

    if isinstance(obj, dict) or isinstance(obj, pd.DataFrame):
        if key:
            return items[selection]

        return obj[items[selection]]

    return items[selection]


def empty_directory(directory_path, excluded_entries: list = None, excluded_filetype: str = None):
    if not excluded_entries:
        excluded_entries = []
    # Check if the directory exists
    if not os.path.exists(directory_path):
        return False

    # List all files and subdirectories in the directory
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        if any(list(filter(lambda file: os.path.splitext(file)[1] == excluded_filetype, filenames))
               for _, _, filenames in os.walk(entry_path, topdown=False)):
            continue

        excluded = filter(lambda excluded_entry: excluded_entry in entry, excluded_entries)
        if any(excluded) or (excluded_filetype and entry.endswith(excluded_filetype)):
            continue

        # Check if it's a file and remove it
        if os.path.isfile(entry_path):
            assert not entry_path.endswith(".py"), f"Trying to delete python (.py) files! ({entry_path})"
            os.remove(entry_path)

        # Check if it's a directory and remove it recursively
        elif os.path.isdir(entry_path):
            shutil.rmtree(entry_path)


def get_data_path(data_current_dir: str = None, file: str = None, exclude_list: list = None, file_format: str = ".csv"):
    if not data_current_dir:
        data_current_dir = os.getcwd()

    if not exclude_list:
        exclude_list = []

    data_path = data_current_dir
    for dirpath, dirnames, filenames in os.walk(data_current_dir):
        # Interactively select which directory for the current household. Returns only one output.
        if dirpath == data_path:
            if dirnames:
                options = list(filter(lambda dir_: dir_ not in exclude_list, dirnames))
                data_path = os.path.join(data_path, select_option(options, "directory"))
            elif file:
                assert file in filenames, f"{file} is not in {dirpath}."
                return data_path, file
            else:
                files = sorted(filter(lambda file_: os.path.splitext(file_)[1] == file_format, filenames))
                file = select_option(files)
                return data_path, file


def get_file_path(current_dir: str = None, file_exts: list = None, extra_options: dict = None,
                  exclude_list: list = None, dir_only: bool = False):
    if not current_dir:
        current_dir = os.getcwd()

    if not exclude_list:
        exclude_list = []

    if not file_exts:
        file_exts = [".csv"]

    while True:
        include_exts = (*file_exts, "")
        options = [option for option in os.listdir(current_dir) if os.path.splitext(option)[1] in include_exts
                   and option not in exclude_list]
        sub_dir = select_option(options, extra_options=extra_options)
        if not sub_dir or os.path.isfile(os.path.join(current_dir, sub_dir)):
            if dir_only:
                return current_dir

            return current_dir, sub_dir

        current_dir = os.path.join(current_dir, sub_dir)
