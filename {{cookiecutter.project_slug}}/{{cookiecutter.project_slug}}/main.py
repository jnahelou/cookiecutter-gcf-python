"""
{{cookiecutter.project_name}}
"""

import logging

def lower(arg: str):
    """
    Set to lower case string provided
    """
    return arg.lower()

def do_some_stuff(arg: str):
    """
    Do a simple stuff
    """
    return lower(arg)

def main(request):
    #pylint: disable=unused-argument
    """
    Main handler used by gcf
    """

    logging.info("Running GCF {{cookiecutter.project_name}}")
    return do_some_stuff("{{cookiecutter.project_name}}")

if __name__ == "__main__":
    main(None)
