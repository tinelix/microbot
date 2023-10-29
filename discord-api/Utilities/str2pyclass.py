import sys

def str2pyclass(classname):
    return getattr(sys.modules[__name__], classname)
