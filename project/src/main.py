import logging
import logging.config
import os

from utils.loader import load

def setup_logging(default_path="../logging.conf",
                  default_level=logging.INFO,
                  env_key="LOG_CFG"):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = f.read()
        logging.config.fileConfig(path)
    else:
        logging.basicConfig(level=default_level)

# Initialize logger for this module
logger = logging.getLogger(__name__)
def main():
    logger.debug("Starting main function")
    logger.info("Starting main function")
    load()


if __name__ == "__main__":
    setup_logging()
    main()
