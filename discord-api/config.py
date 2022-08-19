# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License 2.0 & GNU Affero General Public License v3.0 and higher

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'discord_api': os.environ['DISCORD_TOKEN'],    # Discord API token from system environment
    'owm_api': os.environ['OPENWEATHERMAP_TOKEN']  # for OpenWeatherMap API
}

config = {
    'name': 'Microbot',
    'version': '0.2.6',
    'version_date': '2022-08-19',
    'prefix': '>',
    'accent_def': 0x33b5e5,
    'accent_err': 0xff4444,
    'dev_id': 741883312108339231, # Bot developer ID
    'bugs_ch': 995275176029732894,  # To show a bug report in the console, set the value to 0
}

links = {
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=994906248526970951&permissions=2147862592&scope=bot',
    'support': 'https://discord.gg/saEHAWzYt3',
    'website': 'https://tinelix.github.io',
    'repo': 'https://github.com/tinelix/microbot',
}
