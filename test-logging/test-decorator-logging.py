import logging


def debug(loggername):
    logger = logging.getLogger(loggername)

    def log_(enter_message, exit_message=None):
        def wrapper(f):
            def wrapped(*args, **kargs):
                logger.debug(enter_message)
                r = f(*args, **kargs)
                if exit_message:
                    logger.debug(exit_message)
                return r

            return wrapped

        return wrapper

    return log_


my_debug = debug("my.logger")


@my_debug("enter foo", "exit foo")
def add_numbers(a, b):
    return a + b


# Set the logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

# Test the decorated function
result = add_numbers(5, b=3)
print("Result:", result)



### output
# $ venv/bin/python test-decorator-logging.py 
# DEBUG:my.logger:enter foo
# DEBUG:my.logger:exit foo
# Result: 8