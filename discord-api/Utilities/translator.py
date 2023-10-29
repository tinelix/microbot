#   Tinelix Microbot
#   -------------------------------------------------------------------------------------------
#   Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
#   This program is free software: you can redistribute it and/or modify it under the terms of
#   the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
#   See the following files in repository directory for the precise terms and conditions of
#   either license:
#
#       LICENSE.APACHE
#       LICENSE.AGPL
#
#   Please see each file in the implementation for copyright and licensing
#   information, (in the opening comment of each file).

from Utilities import str2pyclass
from Locales import *
import importlib

def translate(where, str, language):
    print(language)
    locale = importlib.import_module("Locales")
    locale_cls = str2pyclass.str2pyclass(locale, "{0}".format(language))
    locale_cls._tr(where, str)

def getLanguages():
    languages = {'ru_RU': 'Russian', 'en_US': 'English'}
    return languages

def formatDate(datetime, size, language):
    try:
        locale = importlib.import_module("Locales")
        locale_cls = str2pyclass.str2pyclass(locale, "{0}".format(language))
        locale_cls._dt_fmt(datetime, size)
    except:
        return "[{0}|{1}|Error]".format(str, where)

