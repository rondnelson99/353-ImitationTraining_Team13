#! /usr/bin/env python3
# This is like 100% copilot btw
# Get a string presesenting the current date and time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d_%H:%M:%S")

# Get a list of all jpg files in the current directory
import os
files = os.listdir()
jpg_files = [f for f in files if f.endswith('.jpg')]

PROCESSED_DIR = 'processed'

# Zip all the jpg files into a zip file with the current date and time
import zipfile
zipfile_path = os.path.join(PROCESSED_DIR, f'{dt_string}.zip')
with zipfile.ZipFile(zipfile_path, 'w') as zipf:
    for f in jpg_files:
        zipf.write(f)

# Put the jpegs in a folder under processed as well
folder_name = os.path.join(PROCESSED_DIR, f'{dt_string}')
os.mkdir(folder_name)
for f in jpg_files:
    os.rename(f, os.path.join(folder_name, f))
