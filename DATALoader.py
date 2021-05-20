print("Hello my firend")

import argparse, os, sys, shutil, urllib.request, logging
from tqdm import tqdm
import zipfile

DATA_URL = "coffeebreakai.com"

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

#Create progress bar using tqdm

class downloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def downloadURL(url, output_path):
    with downloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to())


#download and extract
if not os.path.exists(SOURCE_PATH):
    #Fetch the data
    if not os.path.exists(SOURCE_PATH + '.zip'):
        downloadURL(DATA_URL, os.path.join(DATA_FOLDER, DATASET_FILENAME))

    #Extract
    logging.info("Extracting: %s", os.path.join(DATA_FOLDER, DATASET_FILENAME))

    try:
        with zipfile.ZipFile(os.path.join(DATA_FOLDER, DATASET_FILENAME), 'r') as zipObj:
            # Extract all the contens
            zipObj.extractall(DATA_FOLDER)

    except zipfile.BadZipFile:
        #redownload
        downloadURL(DATA_URL, os.path.join(DATA_FOLDER, DATASET_FILENAME))
        zipObj.extractall(DATA_FOLDER)
