import logging

def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Create a logger
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.DEBUG)

        # Create a file handler
        file_handler = logging.FileHandler('application.log')
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter and add it to the handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(file_handler)

        # Log at the debug level before executing the function
        logger.debug('Function {} started'.format(func.__name__))

        # Log each variable used in the function at the debug level
        for arg in args:
            logger.debug('Argument: {}'.format(arg))
        for key, value in kwargs.items():
            logger.debug('Keyword Argument - {}: {}'.format(key, value))

        # Call the function
        result = func(*args, **kwargs)

        # Log at the debug level after executing the function
        logger.debug('Function {} completed'.format(func.__name__))

        return result

    return wrapper

@log_decorator
def add_numbers(a, b):
    result = a + b
    return result

# Set the logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

# Test the decorated function
result = add_numbers(a=5, b=3)
print('Result:', result)


#### Output - console
# $ venv/bin/python test-decorator-log-func-input-output-args.py 
# DEBUG:add_numbers:Function add_numbers started
# DEBUG:add_numbers:Keyword Argument - a: 5
# DEBUG:add_numbers:Keyword Argument - b: 3
# DEBUG:add_numbers:Function add_numbers completed
# Result: 8

#### Output - .log
# 2023-11-08 00:21:53,398 - add_numbers - DEBUG - Function add_numbers started
# 2023-11-08 00:21:53,398 - add_numbers - DEBUG - Keyword Argument - a: 5
# 2023-11-08 00:21:53,398 - add_numbers - DEBUG - Keyword Argument - b: 3
# 2023-11-08 00:21:53,398 - add_numbers - DEBUG - Function add_numbers completed
