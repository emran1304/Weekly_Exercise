import logging


def setup_logger(name, log_file, f = '%(asctime)s %(levelname)s %(message)s', console=False, level=logging.DEBUG):
    handler = logging.FileHandler(log_file)
    handler_formatter = logging.Formatter(f)
    handler.setFormatter(handler_formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(log_format)

        logger.addHandler(console_handler)
    return logger
