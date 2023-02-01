import os
import shutil
from zipfile import ZipFile, is_zipfile
from rarfile import RarFile, is_rarfile
from sys import argv


def loop_copy(old_path, new_path, shouldExtract=True, move=False):
    """
    Loop through the old_path and create a new folder for every file extension found
    Place each file with the corresponding file extension into the correct newly created folder
    Can unzip archived files and place them into the correct folders too
    """
    for root, dirs, files in os.walk(old_path):
        for file in files:
            filename, fileext = os.path.splitext(file)
            # Path to file we are currently handling
            filepath = fr"{root}\{file}"
            # Path to directory we will copy TO
            new_dir = fr"{new_path}\{fileext}"
            # Temp path used for unzipped archives
            temp_path = fr"{new_path}\temp"

            if(shouldExtract):
                # Check for zip or rar file
                if(is_rarfile(filepath)):
                    handle_rar(new_path, filepath, temp_path)
                    continue
                elif(is_zipfile(filepath)):
                    handle_zip(new_path, filepath, temp_path)
                    continue
                if not os.path.exists(new_dir):
                    # Create the directory if it doesn't exist
                    os.makedirs(new_dir)

            # File is not zip or rar, so handle like a normal file
            # Move the file or copy the file depending on parameters
            if move:
                shutil.move(filepath, new_dir)
            else:
                shutil.copy(filepath, new_dir)
    # Delete temp folder if it exists
    if(os.path.exists(temp_path)):
        shutil.rmtree(temp_path)


def handle_rar(new_path, filepath, temp_path, move=True):
    """
    Opens and extracts all from the specified rarfile into the temp_path given
    Then calls loop_copy function on the temporary path to place the extracted files into the corresponding folders
    """
    with RarFile(filepath, 'r') as obj:
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        obj.extractall(path=temp_path)

    loop_copy(temp_path, new_path, move)


def handle_zip(new_path, filepath, temp_path, move=True):
    """
    Opens and extracts all from the specified zipfile into the temp_path given
    Then calls loop_copy function on the temporary path to place the extracted files into the corresponding folders
    """
    with ZipFile(filepath, 'r') as obj:
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)
        obj.extractall(path=temp_path)
    loop_copy(temp_path, new_path, move)


def check_paths(old_path, new_path):
    if not os.path.exists(old_path):
        raise Exception(f"Directory not found {old_path}")
    if not os.path.exists(new_path):
        os.makedirs(new_path)


def show_help():
    return """Parameters are:
--h -> Help Screen
--e -> Set this to NOT extract ZIP or RARs
--m -> Set this to MOVE files rather than COPY"""


if __name__ == '__main__' and len(argv) == 1:
    old_path = input("Enter the directory you wish to copy FROM recursively: ")
    new_path = input("Enter the directory you wish to copy TO: ")
    extract = input(
        "Do you want to extract ZIP & RAR files (blank for y)? y/n: ")
    if(extract.lower().startswith("n")):
        extract = False
    else:
        extract = True
    check_paths(old_path, new_path)
    loop_copy(old_path, new_path, shouldExtract=extract)
    print("Success!")
elif __name__ == '__main__' and len(argv) > 1:
    old_path = argv[1]
    if("--h" in old_path):
        print(show_help)
        exit()
    try:
        new_path = argv[2]
    except KeyError:
        raise Exception(
            "Please supply two paths: one to copy FROM and one to copy TO")
    param1 = ""
    param2 = ""
    check_paths(old_path, new_path)
    shouldExtract = True
    shouldMove = False
    try:
        param1 = argv[3]
    except KeyError:
        pass
    try:
        param2 = argv[4]
    except KeyError:
        pass
    if "--h" in [param1, param2]:
        print(show_help())
    if "--e" in [param1, param2]:
        shouldExtract = False
    if "--m" in [param1, param2]:
        shouldMove = True

    loop_copy(old_path, new_path, shouldExtract=shouldExtract, move=shouldMove)
