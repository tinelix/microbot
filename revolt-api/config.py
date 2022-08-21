# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License 2.0 & GNU Affero General Public License v3.0 and higher

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'revolt_api': os.environ['REVOLT_TOKEN'],      # Revolt API token from system environment
    'owm_api': os.environ['OPENWEATHERMAP_TOKEN']  # for OpenWeatherMap API
}

config = {
    'name': 'Microbot',
    'version': '0.2.8 for Revolt',
    'version_date': '2022-08-19',
    'prefix': '.',
    'accent_def': '#33b5e5',
    'accent_err': '#ff4444',
    'dev_id': '01FFKCBK0DXD9G3KDVJ3MV8H31', # Bot developer ID
    'bugs_ch': '',  # To show a bug report in the console, set the value to 0
}

links = {
    'invite': 'https://app.revolt.chat/bot/01GAWYPXPN741ESRZS6T0ZBVGQ',
    'support': 'https://discord.gg/saEHAWzYt3',
    'website': 'https://tinelix.github.io',
    'repo': 'https://github.com/tinelix/microbot',
}
