import logging
import sys


def handle_error(func: callable):
    try:
        func()

    except Exception as e:
        e_type, e_value, e_traceback = sys.exc_info()
        logging.error("Exception type : %s " % e_type.__name__)
        logging.error("Exception message : %s " % e_value.__name__)
        logging.error("Stack trace : %s " % e_traceback.__name__)

        raise e
