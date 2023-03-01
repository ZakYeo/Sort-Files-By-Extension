# Sort-Files-By-Extension
Takes two inputs: directory to copy FROM and a directory to copy TO.<br>
This application will recursively loop through the directory to copy FROM and copy every file into the copy TO directory.<br>
Every file copied into the copy TO directory is sorted by file extension in their respective folder.<br>
The application will also automatically unzip RAR and ZIP files and supports command-line parameters through Python's sys.argv functionality<br>

## Usage:
- Python is required for this to work
- Then install the required library via `pip install rarfile` in the command-line
- You may simply run the Python file e.g by double clicking the file and you will be prompted to enter 2 directories, one to copy FROM and the other to copy TO
- You can also run the Python file via the command line and supply system arguments
- To run via the command line, cd to the directory of the Python file. Then use `py ./sort-files-by-extension.py` and supply optional parameters (see screenshots below)

## Parameters to supply using sys.argv:
- `--h` -> Help Screen <br>
- `--e` -> Set this to NOT extract ZIP or RARs<br>
- `--m` -> Set this to MOVE files rather than COPY<br>

## Images
This image shows execution of the application supplying 2 sysargv arguments: copyFROM path & copyTO path. It automatically extracts the ZIP&RAR contents from copyFROM and places them into their corresponding folder (this case .txt) into the copyTO folder
<img
  src="/images/image_1.png"
  alt="Image 1 of application"
  title="Image 1 of application"
  style="display: inline-block; margin: 0 auto; width: 100%; height: 100%;"> <br>
This image shows the --h parameter output
<img
  src="/images/image_2.png"
  alt="Image 2 of application"
  title="Image 2 of application"
  style="display: inline-block; margin: 0 auto; width: 100%; height: 100%;"><br>
This image displays the execution of the application supplying 4 sysargv arguments
<img
  src="/images/image_3.png"
  alt="Image 3 of application"
  title="Image 3 of application"
  style="display: inline-block; margin: 0 auto; width: 100%; height: 100%;"><br>
This image shows what happens if you run the application normally without supplying sysargv arguments:
<img
  src="/images/image_4.png"
  alt="Image 4 of application"
  title="Image 4 of application"
  style="display: inline-block; margin: 0 auto; width: 100%; height: 100%;"><br>
