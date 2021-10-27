"""This module contains utility functions to start the chess_twist game"""
import sys
import inspect


def main(function):
    """Call function with command line arguments. Used as a decorator.
    The main decorator marks the function that starts a program. For example,
    @main
    def my_run_function():
        # function body
    Use this instead of the typical __name__ == "__main__" predicate.
    """
    if inspect.stack()[1][0].f_locals['__name__'] == '__main__':
        args = sys.argv[1:] # Discard the script name from command line
        function(*args) # Call the main function
    return function
