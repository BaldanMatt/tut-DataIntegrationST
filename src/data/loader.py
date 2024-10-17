from src.utils._constants import MERFISH_MOUSE_BRAIN_DATA, CSV_MAX_ROWS_TO_DISPLAY
import csv
import logging
import logging.config
from src.utils._logging import ColoredFormatter
from itertools import islice

from spatialdata_io import merscope
import spatialdata as sd

import os

# Load the logging configuration from logging.conf
logging.config.fileConfig('logging.conf')

# Get a logger dynamically based on the module name
logger = logging.getLogger(__name__)

def load(slice_number: int = 1,
         replicate_number: int = 1,
         verbose: int = 2):
    if verbose == 0:
        logger.setLevel(logging.ERROR)
    elif verbose == 1:
        logger.setLevel(logging.INFO)
    elif verbose == 2:
        logger.setLevel(logging.DEBUG)

    data_path = MERFISH_MOUSE_BRAIN_DATA / f"Slice{slice_number}" / f"Replicate{replicate_number}"

    logger.info(f"Loading data...")
    logger.debug(f"Loading data from Path: \n{data_path}")

    # Load data here
    # Check if the data is already converted in .zarr format
    if not os.path.exists(data_path / "data.zarr"):
        # the following function comes from spatialdata-io and reads vizgen data
        tmp = merscope(data_path) # many options in reading the vizgen data
        tmp.write(data_path / "data.zarr")
        del tmp
    
    # read the .zarr data file
    sdata = sd.read_zarr(data_path / "data.zarr")    

    logger.debug(f"Loaded data:\n{sdata}")
    logger.info(f"Data loaded successfully.")
    
    return sdata
if __name__ == "__main__":
    load(verbose=2)

    
