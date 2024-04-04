import argparse
import os
import subprocess

#TODO: better help messages
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", default=".",
                    help =  "(relative) path to image. can be a file or a directory")

parser.add_argument("-W", "--width", default=False, dest="--width",
                    help =  "set width of ascii art, height is generated automatically to\
                            keep aspect ratio")

parser.add_argument("-d", "--dimensions", default=False, dest="--dimensions",
                    help =  "dimensions of the generated image. A good value is probably\
                            80,40")

parser.add_argument("-s", "--save-txt", default=False, dest="--save-txt",
                    help =  "give the (relative) path to where pictures should be saved.\
                            If the path already exists, errors")

parser.add_argument("--only-save", action="store_true", dest="--only-save",
                    help =  "save but doesn't output image")

parser.add_argument("-C", "--csv", default=False, dest="--csv",
                    help =  "save a csv file with filenames corresponding to classes\
                            in specified file. only works if file is created in\
                            an existing dir")

parser.add_argument("-a", "--animal-dict", default=False, dest="--animal-dict",
                    help =  "create a little csv file that contains a dict of which\
                            animal corresponds to which feature number. Only\
                            works if file is created in an existing dir")

converter_args = ["--width", "--dimensions", "--save-txt", "--only-save"]
args = parser.parse_args()
processed_converter_args = ["ascii-image-converter", args.path]

processed_args = {}

for key, word in vars(args).items():
    if key in converter_args: # process vars for ascii converter tool
        if type(word)==bool:
            if word:
                processed_converter_args.append(key)
        else:
            processed_converter_args.append(key)
            processed_converter_args.append(word)
    # also make a dict of processed args
    processed_args[key] = word


# check that not both --width and --dimensions were set
assert not ("--width" in processed_converter_args and "--dimensions" in processed_converter_args)\
, "cannot set both --width and --dimensions flags"
