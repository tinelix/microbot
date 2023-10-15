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

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'revolt_api': os.environ['REVOLT_TOKEN'],      # Revolt API token from system environment
    'owm_api': os.environ['OPENWEATHERMAP_TOKEN']  # for OpenWeatherMap API
}

config = {
    'name': 'Microbot',
    'version': '0.3.2 for Revolt',
    'version_date': '2022-08-20',
    'prefix': '.',
    'accent_def': '#33b5e5',
    'accent_err': '#ff4444',
    'dev_id': '01FFKCBK0DXD9G3KDVJ3MV8H31', # Bot developer ID
    'bugs_ch': '',  # To show a bug report in the console, set the value to 0
}

links = {
    'invite': 'https://app.revolt.chat/bot/01GAWYPXPN741ESRZS6T0ZBVGQ',
    'support': '',
    'website': 'https://tinelix.github.io',
    'repo': 'https://github.com/tinelix/microbot',
}
