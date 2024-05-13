import logging

def init_logger():
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('main_test.log')
    logger = logging.getLogger('selenium')
    logger.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = init_logger()

def log_info(error_mesage):
    def decorator(func):
        def wrapper(*args, **kwargs):
            formatted_err_msg = ''
            
            if len(args) >= 3:
                formatted_err_msg = error_mesage.format(link=args[1], locator=args[1], text=args[2])
            elif len(args) >= 2:
                formatted_err_msg = error_mesage.format(link=args[1], locator=args[1])

            logger.info(formatted_err_msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator