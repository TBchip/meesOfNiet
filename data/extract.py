import os
from PIL import Image, ImageOps

def add_folder(csv_file, folder_path):
    for filename in os.listdir( folder_path ):
        file_path = os.path.join(folder_path, filename)
        if(os.path.isdir(file_path)):
            add_folder(csv_file, file_path)
            continue
        
        print(filename)
        img = Image.open(file_path)
        img = img.resize((128,128), Image.ANTIALIAS)
        img = ImageOps.grayscale(img)
        img_arr = [round(i/255, 3) for i in img.getdata()]

        line = '\n'
        line += '1' if file_path.find('ThijsBischoff') != -1 else '0'
        print(file_path.find('ThijsBischoff'), len(img_arr))
        for i in img_arr:
            line += ','+str(i)

        csv_file.write(line)

csv = open('thijsBischoff.csv', 'a')

line = 'Thijs_Bischoff'
for i in range(128*128):
    line += ',pix-'+str(i)
csv.write(line)

add_folder(csv, os.path.join(os.getcwd(), 'ThijsBischoff'))
add_folder(csv, os.path.join(os.getcwd(), 'other'))