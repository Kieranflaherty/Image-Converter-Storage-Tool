# **Image Converter & Storage Tool  

This program reduces the size of the saved images by converting them from bmp to jpg and then creates a daily archive of images each day which allows the images to be stored for the long term. The scripts are developed in Python and run off a batch file controlled by Windows Task Scheduler. This was used in a production environment on Cognex Vision Systems which are used for capturing images 

**Image Converter

This convert script can be used for any folder where images are being generated and need to be compressed to consume less storage. the tool converts the images to approximately 20 times smaller than their original size without affecting image quality or their appearance, the pyhiscal size of the image will not change just the storage size. The script "Convert_2_Jpg.py will carry out this action and can be used by simply editing the file paths to suit your environment. You can also change the extension in case you are converting different image formats.

**File Archive System

This script can be used to transfer files from a specified folder to another specified location. In this scenario it was used on a daily scheduled task to transfer the images from that day to a folder elswhere with the following name layout - "CAMERA_NAME_DD_MM_YYYY". The file name can be edited within the code too.


