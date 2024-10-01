from constants import MERFISH_MOUSE_BRAIN_DATA
import logging
import csv

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
    logger.debug(f"Loading data from Path: {data_path}")

    # Load data here
    with open(data_path / "cell_metadata_S1R1.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            logger.debug(row)   

if __name__ == "__main__":
    logger 
    load()