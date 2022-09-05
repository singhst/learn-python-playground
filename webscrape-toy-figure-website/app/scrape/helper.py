

from datetime import datetime
import os
from typing import Union
from bs4 import BeautifulSoup

import pandas as pd


class commonHelper():

    def logger(self):
        from app.main_webscrapping import mainLogger
        return mainLogger


    def _saveFile(self, data: Union[pd.DataFrame, BeautifulSoup],
                shop: str,
                folder: str,
                filename: str,
                data_type: str = 'csv',
                ):
        yyyymmdd = datetime.now().strftime('%Y%m%d')
        path = f"{folder}/{data_type}/shop={shop}/dt={yyyymmdd}/"
        filename = f"{filename}_{yyyymmdd}.{data_type}"
        save_path = f"{path}/{filename}"
        self._checkFolderPath(path)
        
        {
            # immediately invoked function
            "csv": lambda f: data.to_csv(save_path, index=False),
            "json": lambda f: data.to_json(save_path, orient='records', lines=True, force_ascii=False),    #one-line json
            "html": lambda f: open(save_path, mode='wt', encoding='utf-8').write(str(data)),
        }.get(data_type)('')


    def _checkFolderPath(self, folder_path: str):
        # Create a new directory because it does not exist 
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            self.logger().debug(">>> Created folder: {}".format(folder_path))


"""
=== Testing Zone Below ========================================================
"""

# Decorator to print function call
# details
def function_details(func):
    
    
    # Getting the argument names of the
    # called function
    argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
    
    # Getting the Function name of the
    # called function
    fname = func.__name__
    
    
    def inner_func(*args, **kwargs):
        
        print(fname, "(", end = "")
        
        # printing the function arguments
        print(', '.join( '% s = % r' % entry
            for entry in zip(argnames, args[:len(argnames)])), end = ", ")
        
        # Printing the variable length Arguments
        print("args =", list(args[len(argnames):]), end = ", ")
        
        # Printing the variable length keyword
        # arguments
        print("kwargs =", kwargs, end = "")
        print(")")
        
    return inner_func




import sys

class debug_context():
    """ Debug context to trace any function calls inside the context """

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Entering Debug Decorated func')
        # Set the trace function to the trace_calls function
        # So all events are now traced
        sys.settrace(self.trace_calls)

    def __exit__(self, *args, **kwargs):
        # Stop tracing all events
        sys.settrace = None

    def trace_calls(self, frame, event, arg): 
        # We want to only trace our call to the decorated function
        if event != 'call':
            return
        elif frame.f_code.co_name != self.name:
            return
        # return the trace function to use when you go into that 
        # function call
        return self.trace_lines

    def trace_lines(self, frame, event, arg):
        # If you want to print local variables each line
        # keep the check for the event 'line'
        # If you want to print local variables only on return
        # check only for the 'return' event
        if event not in ['line', 'return']:
            return
        co = frame.f_code
        func_name = co.co_name
        line_no = frame.f_lineno
        filename = co.co_filename
        local_vars = frame.f_locals
        print ('  {0} {1} {2} locals: {3}'.format(func_name, 
                                                  event,
                                                  line_no, 
                                                  local_vars))


def debug_decorator(func):
    """ Debug decorator to call the function within the debug context """
    def decorated_func(*args, **kwargs):
        with debug_context(func.__name__):
            return_value = func(*args, **kwargs)
        return return_value
    return decorated_func