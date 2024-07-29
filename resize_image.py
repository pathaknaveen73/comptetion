import os,sys
from os import listdir
from os.path import isfile, join
from PIL import Image
from resizeimage import resizeimage


try:
    
    img_path = os.getcwd()+"/"+sys.argv[1]+"/"
    print (img_path)
    download_path = os.getcwd()+"/"+ sys.argv[1]+"_resize/"


    onlyfiles = []
    onlyfiles = [f for f in listdir(img_path) if isfile(join(img_path, f))]
    c=0
    if not os.path.exists(download_path):
        os.makedirs(download_path)
except Exception as e:
    print ("Error ---- ",e)
    exit()

for i in onlyfiles:
    c = c+1
    print (c," ",i)
    try:
        with open(img_path+i, 'r+b') as f:
            with Image.open(f) as image:
                image.thumbnail((80, 80))
                image.save(download_path+i, image.format)
    except Exception as e:
        print ("Exception occured ----> ",e)
        print ("All images resized to --- ",download_path)