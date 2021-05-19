print("Hello my firend")

import argparse, os, sys, shutil, urllib.request, logging
from tqdm import tqdm
import zipfile

DATA_URL = ""

#Folder where to store all data
DATA_FOLDER = "TRainingImages"

SOURCE_PATH = os.path.join(DATA_FOLDER, "img_test")

#FIle name for DATASET
DATASET_FILENAME = os.path.basename(DATA_URL)

#Destination directory
DEST_PATH = os.path.join(DATA_FOLDER, "DF")
##########################################################

parser = argparse.ArgumentParser(description="Dataset folder")
parser.add_argument('-d', '--debug', default=False, action="store_true", help='Print debug spew')
args = parser.parse_args()

#Logging init
logging.getLogger(args.debug)

#Create a datafolder if it does not exist yet!
if not os.path.exists(DATA_FOLDER):
    try:
        os.mkdir(DATA_FOLDER)
    except OSError:
        logging.info("Creating the directory is %s failed")
    else:
        logging.debug("Successfully created the directroy: %s", DATA_FOLDER)



