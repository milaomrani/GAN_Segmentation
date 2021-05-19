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