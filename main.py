import os
from os import path


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

def create_hdpi(main_path,photo_path):
    img = Image.open(photo_path)
    ic_launcher = img.resize((72,72))








def main(photo_dir,finish_dir):
    name = photo_dir.split('/')[-1].split('.')[0]
    main_path = create_dirs(finish_dir,name)


if __name__ == "__main__":
    FINISH_DIR = '/root/PycharmProjects/generate_fhoto/result'
    PHOTO_DIR = '/252098.jpg'
    main(PHOTO_DIR,FINISH_DIR)