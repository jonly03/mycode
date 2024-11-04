#!/usr/bin/env python3
"""
A multi-line comment to describe the script,
made with triple quotes
"""

def main(): # all code should appear within a function
    """
    all functions have multiline comments to describe them
    """
    my_string = "you code could go here" #vars use _ (snake_case) instead of camelCase
    print(my_string) #print to standard-out

# calling main() using this technique allows others to import your code
if __name__ == "__main__": # when a .py file is being run directly the built-in __name__ variable is set to __main__. This allows us to ensure that when the file is imported, main doesn't run
    main()