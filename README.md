
# mischief-managed

A simple script to tidy files lying outside of folders based on extension and date modified.

No deletions, simple moving of stray files into appropriate subfolders

## WHY?
If you are like an average desktop/laptop user, you have lots of stray files in various locations in your system, especially in the downloads section.

To solve this, `mischief-managed` create a subfolder according to the type specified by the user. Current options are extension or date based. All files are then moved into appropriate subfolders.

## Setup
To use, install by entering into command line -

    pip install mischief-managed

View Pypi project on https://pypi.org/project/mischief-managed/

##  Usage

**Simple usage** - 

    mischief-managed
Just this command will manage the current working directory.

**Complete options** - 

    usage: mischief-managed [-h] [--path PATH] [--ext EXT] [--use-def] [--date] [-r RECENT]

**Optional arguments:**

  **-h, --help**  :  show this help message and exit.
  
  **--path PATH**  :  Directory to manage or target, instead of the current working directory.
  
  **--ext EXT**  :  Flag if to tidy the files into the extension based folders.
  
  **--use-def**  :  Flag to use general folder name like 'Images' for extensions - jpg,png etc.
                For custom general name for subfolders,  see `variables.py` and change according to your need.
		
  **--date**  :  Flag if to tidy the files into the date based folders
  
  **-r RECENT, --recent RECENT**  :  Give the number of files to include in recently created files

## Example usage

- **To create extension based folders like `jpg`, `exe` etc**

	    mischief-managed --path=C:\Users\Downloads\

- **To create extension based folders but with defined general names like `Images` for `jpg`, `Applications` for `exe` etc**

	    mischief-managed --path=C:\Users\Downloads\ --use-def
See `variables.py` for defined general names.

- **To create folders based on the last modified date and also a separate folder for some number, say `10`, of recent files.**

	  mischief-managed --path=C:\Users\Downloads\ --recent=10

**System image**

Before - 

![files_capture](PREVIEW/files_capture.JPG?raw=true)

After - 

![folder_capture](PREVIEW/folder_capture.JPG?raw=true)


**Open for any constructive Contribution.**

**Future Feature** - A feature to undo the effect of this, can be added. Just submit a feature request and it will be added.

**Made by Help-a-Sloth org.**

