# converter used: https://github.com/TheZoraiz/ascii-image-converter
# dataset used: https://www.kaggle.com/datasets/alessiocorrado99/animals10

import os
import subprocess
from os.path import isfile

path = "dataset/raw-img/"
#ascii_path = "./dataset/ascii-img/"
ascii_path = "./dataset/ascii-img-uniform-size/"
classes = os.listdir(path)


i=0
for animals in classes:
    # print first ten animals in classes
    print(animals)
    for animal in os.listdir(path+animals):
        
        # test if working
        file = path+animals+"/"+animal
        if (os.path.isfile(file)):
            subprocess.run(["ascii-image-converter", file, "-W", "80",  "--save-txt", ascii_path+animals])
            #print(subprocess.run(["ls", "-l"]))
        i+=1
    i=0
