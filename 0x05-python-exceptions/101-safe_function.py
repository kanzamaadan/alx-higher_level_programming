#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        excute = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
    return excute
