from PIL import Image
from os import listdir,path
import os

file_path = '.'
file_format = '.bmp'
for file in listdir(file_path):
    file_name, file_type = path.splitext(file)
    try:
        if file_type not in [file_format, '.py','.png','.svg']:
            im = Image.open(file_name + file_type)
            im.save(file_name + file_format)
        print('Converted: {} Conversion'.format(file))
    except (IOError, OSError):
        print('Error: {} Conversion'.format(file))

for file in os.listdir('.'):
    if file.endswith('.jpg'):
        os.remove(file)
