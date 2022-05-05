import os
from os import path
from sys import argv
from PIL import Image, ImageDraw, ImageFilter

def create_dirs(finish_dir,name):
    res_path = path.join(finish_dir,name)
    if path.exists(res_path) == False:
        os.mkdir(res_path)
        os.mkdir(path.join(res_path,'mipmap-hdpi'))
        os.mkdir(path.join(res_path, 'mipmap-mdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xhdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xxhdpi'))
        os.mkdir(path.join(res_path, 'mipmap-xxxhdpi'))
    return res_path

def create_elipce(img,size):
    img = img.resize((size, size))
    im_a = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(im_a)
    shape = [(0, 0), (size, size)]
    draw.ellipse(shape, fill=255)
    im_rgba = img.copy()
    im_rgba.putalpha(im_a)
    return im_rgba

def create_rectangle(img,size):
    img = img.resize((size, size))
    im_a = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(im_a)
    shape = [(0, 0), (size, size)]
    draw.rounded_rectangle(shape,radius=10, fill=255)
    im_rgba = img.copy()
    im_rgba.putalpha(im_a)
    return im_rgba

def change_size(size,img):
    img = img.resize((size, size))
    return img

def create_pack(main_path,photo_path,folder_name,small_size,big_size):
    current_path = path.join(main_path,folder_name)
    img = Image.open(photo_path)
    img_eliphe = create_elipce(img,small_size)
    img_eliphe.save(current_path+"/ic_launcher_round.png")
    img_rectangle = create_rectangle(img,small_size)
    img_rectangle.save(current_path+"/ic_launcher.png")
    img_size = change_size(big_size,img)
    img_size.save(current_path+'/ic_launcher_foreground.png')

def main(photo_dir,finish_dir):
    name = photo_dir.split('/')[-1].split('.')[0]
    main_path = create_dirs(finish_dir,name)
    data = [{'folder_name':'mipmap-hdpi','big_size':162,'small_size':72},
            {'folder_name':'mipmap-mdpi','big_size':108,'small_size':48},
            {'folder_name':'mipmap-xhdpi','big_size':216,'small_size':96},
            {'folder_name':'mipmap-xxhdpi','big_size':324,'small_size':144},
            {'folder_name':'mipmap-xxxhdpi','big_size':432,'small_size':192}]
    for d in data:
        create_pack(main_path,photo_dir,d['folder_name'],d['small_size'],d['big_size'])



if __name__ == "__main__":
    name,finish_dir , photo_dir = argv
    FINISH_DIR = '/home/ubuntu/PycharmProjects/generate_fhoto/result'
    PHOTO_DIR = '/home/ubuntu/PycharmProjects/generate_fhoto/252098.jpg'
    main(photo_dir,finish_dir)