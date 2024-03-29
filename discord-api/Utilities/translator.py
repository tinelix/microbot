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
    locale = importlib.import_module("Locales.{0}".format(language))
    string = locale._tr(where, str)
    importlib.invalidate_caches()
    return string

def getLanguages():
    languages = {'ru_RU': 'Russian', 'en_US': 'English'}
    return languages

def formatDate(datetime, size, language):
    try:
        locale = importlib.import_module("Locales.{0}".format(language))
        string = locale._dt_fmt(datetime, size)
        importlib.invalidate_caches()
        return string
    except:
        return "[{0}|{1}|Error]".format(str, where)

