### This program takes the files in the archive folder and converts all the bmp files to jpg ####

from PIL import Image
from os import listdir,path
import os
from datetime import datetime

today = datetime.now()
file_path = "E:\Vision\BDB040501_St25_Lower\Bad\BDB040501_St25_Lower_" + today.strftime('%Y_%m_%d')
file_format = '.jpg'

for filename in os.listdir(file_path):
    full_path = os.path.join(file_path, filename)
    file_name, file_type = path.splitext(full_path)
    try:
        if file_type not in [file_format, '.py','.png','.svg']:
            im = Image.open(file_name + file_type)
            im.save(file_name + file_format)
            print('Converted: {} Conversion'.format(filename))
    except (IOError, OSError):
        print('Error: {} Conversion'.format(filename))

for filename in os.listdir(file_path):
    full_path = os.path.join(file_path, filename)
    if filename.endswith(".bmp"):
        os.remove(os.path.join(file_path, filename))
