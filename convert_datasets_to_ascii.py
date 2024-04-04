# converter used: https://github.com/TheZoraiz/ascii-image-converter
# dataset used: https://www.kaggle.com/datasets/alessiocorrado99/animals10

import os
import subprocess
import datapreprocessing_argparse as dp
import csv
import pathlib

img_path = dp.args.path 
save_path = dp.processed_args["--save-txt"]
csv_path = dp.processed_args["--csv"]
classes = os.listdir(img_path)
animal_dict_path = dp.processed_args["--animal-dict"]

# make save dir
os.makedirs(save_path)

# to iterate between features in csv writing
feature = 0

# list of args to be passed to ascii converter
args = dp.processed_converter_args

if csv_path:
    csvfile = open(csv_path, "w", newline="")
    writer = csv.writer(csvfile, delimiter=",")
if animal_dict_path:
    animal_dict_file = open(animal_dict_path, "w", newline="")
    animal_dict_writer = csv.writer(animal_dict_file, delimiter=",")
for animals in classes:
    if animal_dict_path:
        animal_dict_writer.writerow([animals, feature])
    for animal in os.listdir(os.path.join(img_path, animals)):
        filepath = os.path.join(img_path, animals, animal)
        if (os.path.isfile(filepath)):
            args[1] = filepath
            # transform
            subprocess.run(args)
            # write to csv file
            # remove file extension and replace with -ascii-art.txt
            if csv_path:
                ascii_animal = pathlib.Path(animal).stem + "-ascii-art.txt"
                writer.writerow([ascii_animal, feature])
    # move on to next feature
    feature += 1;
if csv_path:
    csvfile.close()
if animal_dict_path:
    animal_dict_file.close()
