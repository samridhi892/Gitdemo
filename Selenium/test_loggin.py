import logging


def test_logging():
    logger = logging.getLogger(__name__)

    filehandle = logging.FileHandler("file_log.log")  #declaring the file name when the logs will be placed
    formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  #format of the log file
    filehandle.setFormatter(formater)

    logger.addHandler(filehandle)  # where the log File needs to be placed.

    logger.setLevel(logging.INFO)  # setting the level , setting to INFO will print out log only from INFO and not from DEBUG, even if debug is mentioned again, if its set from error, it will print from erro and not from above
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Warning mode ")
    logger.error("A major error has happened")
    logger.critical("Critical issue")
