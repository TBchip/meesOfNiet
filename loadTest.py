import pandas as pd
import os
from PIL import Image, ImageOps
from keras.models import load_model

csv_path = 'data/test.csv'
imgs_path = 'data/test/'

model_name = 'tfmodel_mees'

def formatImgsToCsv(csv, folder_path):
    original_imgs = []

    for filename in os.listdir( folder_path ):
        file_path = os.path.join(folder_path, filename)
        if(os.path.isdir(file_path)):
            original_imgs += formatImgsToCsv(csv, file_path)
            continue

        print(filename, ' loading...')

        img = Image.open(file_path)
        original_imgs.append(img)

        img = img.resize((128,128), Image.ANTIALIAS)
        img = ImageOps.grayscale(img)

        img_arr = [str(round(i/255, 3)) for i in img.getdata()]

        line = ','.join(img_arr)+'\n'

        csv.write(line)

    return original_imgs

open(csv_path, 'w').close()
csv = open(csv_path, 'a')

lineArr = []
for i in range(128*128):
    lineArr += ['pix-'+str(i)]
line = ','.join(lineArr)+'\n'
csv.write(line)

imgs = formatImgsToCsv(csv, os.path.join(os.getcwd(), imgs_path))

df = pd.read_csv(csv_path)

print(df)

model = load_model(model_name)
pred = model.predict(df)


for i in range(len(imgs)):
    os.system('cls')

    answer = 'Mees' if pred[i][0] >= 0.5 else 'niet Mees'
    print('De volgende foto is', answer)
    input('Druk op enter om de foto te zien...')
    print()

    imgs[i].show()

    input('Druk op enter om naar de volgende foto te gaan...')