import os
from os import path


def create_dirs(finish_dir,name):
    os.mkdir(name)







def main(photo_dir,finish_dir):
    name = photo_dir.split('/')[-1].split('.')[0]
    create_dirs(finish_dir,name)


if __name__ == "__main__":
    FINISH_DIR = 'result'
    PHOTO_DIR = '/252098.jpg'
    main(PHOTO_DIR,FINISH_DIR)