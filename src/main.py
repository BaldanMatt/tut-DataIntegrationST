import logging
# Load the logging configuration from logging.conf
logging.config.fileConfig('logging.conf')

# Get a logger dynamically based on the module name
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting the main function")

    #TODO: loading framework
    from data.loader import load

    #TODO: spatial + scRNAseq framework

    #TODO: Launch DecoupleR framework

    #TODO: data analysis framework 



    logger.info("Finished the main function")

if __name__ == "__main__":
    main()
