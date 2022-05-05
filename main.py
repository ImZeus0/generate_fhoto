import os
from os import path
from sys import argv
from PIL import Image, ImageDraw, ImageFilter
import numpy
import numpy as np


def create_dirs(finish_dir, name):
    res_path = path.join(finish_dir, name)
    if path.exists(res_path) == False:
        os.mkdir(res_path)
        os.mkdir(path.join(res_path, 'mipmap-hdpi'))
        os.mkdir(path.join(res_path, 'mipmap-mdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xhdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xxhdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xxxhdpi'))
        os.mkdir(path.join(res_path, '_MACSOX'))
        os.mkdir(path.join(res_path, '_MACSOX/values'))
        os.mkdir(path.join(res_path, 'values'))
    return res_path


def create_elipce(img, size):
    img = img.resize((size, size))
    im_a = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(im_a)
    shape = [(0, 0), (size, size)]
    draw.ellipse(shape, fill=255)
    im_rgba = img.copy()
    im_rgba.putalpha(im_a)
    return im_rgba


def create_rectangle(img, size):
    img = img.resize((size, size))
    im_a = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(im_a)
    shape = [(0, 0), (size, size)]
    draw.rounded_rectangle(shape, radius=10, fill=255)
    im_rgba = img.copy()
    im_rgba.putalpha(im_a)
    return im_rgba


def change_size(size, img):
    img = img.resize((size, size))
    return img


def create_pack(main_path, photo_path, folder_name, small_size, big_size):
    current_path = path.join(main_path, folder_name)
    img = Image.open(photo_path)
    img_eliphe = create_elipce(img, small_size)
    img_eliphe.save(current_path + "/ic_launcher_round.png")
    img_rectangle = create_rectangle(img, small_size)
    img_rectangle.save(current_path + "/ic_launcher.png")
    img_size = change_size(big_size, img)
    img_size.save(current_path + '/ic_launcher_foreground.png')


def dominant_color(filename):
    image = Image.open(filename)
    dominant_color = numpy.array(image.histogram(), dtype=np.int32).reshape(-1, 256).argmax(axis=1)
    strs = '#'
    for i in dominant_color:
        num = int(i)  # включить
        # Перевести R, G и B на 16-контактную конверсию и прописную
        strs += str(hex(num))[-2:].replace('x', '0').upper()
    return strs


def create_color_file(main_path, color):
    text = f"""<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">{color}</color>
</resources>
    """
    with open(main_path+"/values/ic_launcher_background.xml",'a') as w:
        w.write(text)
    with open(main_path+"/_MACSOX/values/.ic_launcher_background.xml",'a') as w:
        w.write(text)


def main(photo_dir, finish_dir):
    color = dominant_color(photo_dir)
    name = photo_dir.split('/')[-1].split('.')[0]
    main_path = create_dirs(finish_dir, name)
    create_color_file(main_path,color)
    data = [{'folder_name': 'mipmap-hdpi', 'big_size': 162, 'small_size': 72},
            {'folder_name': 'mipmap-mdpi', 'big_size': 108, 'small_size': 48},
            {'folder_name': 'mipmap-xhdpi', 'big_size': 216, 'small_size': 96},
            {'folder_name': 'mipmap-xxhdpi', 'big_size': 324, 'small_size': 144},
            {'folder_name': 'mipmap-xxxhdpi', 'big_size': 432, 'small_size': 192}]
    for d in data:
        create_pack(main_path, photo_dir, d['folder_name'], d['small_size'], d['big_size'])


if __name__ == "__main__":
    name, finish_dir, photo_dir = argv
    FINISH_DIR = '/home/ubuntu/PycharmProjects/generate_fhoto/result'
    PHOTO_DIR = '/home/ubuntu/PycharmProjects/generate_fhoto/252098.jpg'
    main(photo_dir, finish_dir)
