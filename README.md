# Anti-Duplicator

Find duplicate of files on directory tree (by name and file size)

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash
$ python duplicates.py <path_to_dir>
```

## Output example:

```bash
$ python duplicates.py c:\adb
File name: adb.exe  File size: 0 - Duplicate list: ['c:\\adb\\adb.exe', 'c:\\adb\\test\\adb.exe', 'c:\\adb\\test2\\adb.exe']
File name: adb.exe  File size: 2 - Duplicate list: ['c:\\adb\\test3\\adb.exe', 'c:\\adb\\test4\\adb.exe']
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
