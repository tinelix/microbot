import sys

def str2pyclass(module, classname):
    return getattr(module, classname)
