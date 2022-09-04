# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Repo: https://github.com/den4ikbot/den4ikbot
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher.

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'discord_api': os.environ['DISCORD_TOKEN'],    # Discord API token from system environment
}

config = {
    'name': 'Den4ik Bot',
    'version': '0.3.1',
    'version_date': '2022-08-31',
    'prefix': '+',
    'accent_def': 0xa55bfd,
    'accent_err': 0xff4444,
    'dev_id': 996078160141631530, # Bot developer ID
    'codev_id': 741883312108339231, # Bot codeveloper ID
    'bugs_ch': 0,  # To show a bug report in the console, set the value to 0
    'cooldown': 1.5
}

links = {
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=1009762625158127636&permissions=2147862592&scope=bot',
    'support': 'https://discord.gg/fHStmPJ35W',
    'website': '',
    'repo': 'https://github.com/den4ikbot/den4ikbot',
    'youtube': 'https://www.youtube.com/channel/UCmliSc1cdfogZHeGb_UJdfw'
}
