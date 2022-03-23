import os
from PIL import Image, ImageOps


def add_folder(csv_file, folder_path, amount=0):
    for filename in os.listdir( folder_path ):
        file_path = os.path.join(folder_path, filename)
        if(os.path.isdir(file_path)):
            amount = add_folder(csv_file, file_path, amount)
            continue
            
        amount += 1
        print(amount)

        img = Image.open(file_path)
        img = img.resize((128,128), Image.ANTIALIAS)
        img = ImageOps.grayscale(img)
        img_arr = [round(i/255, 3) for i in img.getdata()]

        line = '\n'
        line += '1' if file_path.find('Mees') != -1 else '0'
        for i in img_arr:
            line += ','+str(i)

        csv_file.write(line)
    
    return amount

csv = open('Mees.csv', 'a')

line = 'Mees'
for i in range(128*128):
    line += ',pix-'+str(i)
csv.write(line)

meesAmount = add_folder(csv, os.path.join(os.getcwd(), 'Mees'))
print()
input(meesAmount)

notMeesAmount = add_folder(csv, os.path.join(os.getcwd(), 'other'))

print()
print(meesAmount, notMeesAmount)