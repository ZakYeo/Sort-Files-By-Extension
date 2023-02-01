# Sort-Files-By-Extension
Takes two inputs: directory to copy FROM and a directory to copy TO.<br>
This application will recursively loop through the directory to copy FROM and copy every file into the copy TO directory.<br>
Every file copied into the copy TO directory is sorted by file extension in their respective folder.<br>
The application will also automatically unzip RAR and ZIP files and supports command-line parameters through Python's sys.argv functionality<br>

## Usage:
- Python is required for this to work
- You may simply run the Python file e.g by double clicking the file and you will be prompted to enter 2 directories, one to copy FROM and the other to copy TO
- You can also run the Python file via the command line and supply system arguments
- To run via the command line, cd to the directory of the Python file. Then use `py ./sort-files-by-extension.py` and supply optional parameters
