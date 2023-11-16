async def gen_config_file():
    if config['license'] == None:
        print("""\
 Before you launch the bot, you must select a license to distribute and/or create derivative works
 (for example, source code based Microbot modifications).

 \033[92m1. Apache License 2.0 & AGPLv3 or later version (default)
 \033[0m    Requires the public release of modifed source code and provides the same choice.

 2. AGPLv3 or later version
    Requires the public release of modifed source code.

 3. Apache License 2.0
    Useful mainly for beginner developers. Anyone can view the source code and create a derivative
    work without worrying about changes to the source code.
""")
        license_choice = int(input(" Your choice (1-3):"))
        with open("config.py.example", "w") as file:
            file = """# Microbot Discord bot
# Generated 'config.py' file example.
#
# READ COMMENTS PLEASE BEFORE RENAMING & USING THIS FILE

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {
    'discord_api': os.environ['DISCORD_TOKEN'],    # Discord API token from system environment
    'owm_api': os.environ['OPENWEATHERMAP_TOKEN']  # for OpenWeatherMap API
}

config = {
    'name': 'Microbot',             # Your bot name
    'prefix': '>',                  # Your prefix
    'accent_def': 0x33b5e5,         # Your default accent color in embed (inspired by Android Holo design)
    'accent_err': 0xff4444,         # Your accent color if error occured (inspired by Android Holo design)
    'dev_id': 0,                    # Bot developer ID
    'bugs_ch': 0,                   # To show a bug report in the console, set the value to 0
    'cooldown': 1.5 # in seconds
    'license': {0}
}

links = {
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=[Your_Bot_ID]&permissions=2147862592&scope=bot',
    'support': 'https://discord.gg/saEHAWzYt3',
    'website': '[Your_Personal_Website]',
    'repo': 'https://github.com/tinelix/microbot',
    'donate': '[Your_Donate_Link_Here]'
}
""".format(license_choice)
