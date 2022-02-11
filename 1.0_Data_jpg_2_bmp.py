from PIL import Image
from os import listdir,path
import os

file_path = 'C:/Python/Image Compressor/'
file_format = '.bmp'
for file in listdir(file_path):
    file_name, file_type = path.splitext(file)
    try:
        if file_type not in [file_format, '.py','.png','.svg']:
            im = Image.open(file_name + file_type)
            im.save(file_name + file_format)
            for file in os.listdir('.'):
                if file.endswith('.jpg'):
                    os.remove(file)
    except (IOError, OSError):
        print('Converted: {} Conversion'.format(file))
