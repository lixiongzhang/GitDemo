import tkinter
from tkinter import filedialog
import os
from datetime import datetime



today = datetime.now().date()
print('today is ', today)
directory = tkinter.filedialog.askdirectory()
print(directory)
os.chdir(directory)
files = os.listdir(directory)
for file in files:
    in_file = open(file, 'rb')
    image = in_file.read()
    in_file.close()
    image = bytearray(image)
    key = 46
    for index, value in enumerate(image):
        image[index] = value ^ key
    save_path = r'C:/test/'
    s = file.split("/")
    file = s[-1]
#    os.chdir(save_path)
    out_filename = os.path.join(save_path, file + ' ' + str(today) + '.enc')
    print(out_filename)
    out_file = open(out_filename, 'wb')
    out_file.write(image)
#    os.startfile(save_path)
    out_file.close()
print(directory)
print(files)