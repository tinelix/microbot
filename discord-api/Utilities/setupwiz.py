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

def gen_config_file(sys, config, links):
    if 'license' not in config or config['license'] == 0:
        print("""Before the first launch of Microbot, you must select a license to distribute and create derivative works
 (for example, source code based Microbot modifications).

 \033[92m1. Apache License 2.0 & Affero GPLv3 or later version (recommended)
 \033[0m   Requires public release of modified source code (as with GPLv3) and gives developers the same choice.

 2. Affero GPLv3 or later version
    Requires the public release of modifed source code.

 3. Apache License 2.0
    Useful mainly for beginner or inexperienced developers. Anyone can view the source code and create a
    derivative work without worrying about changes to the source code.
""")
        license_choice = int(input(" Your choice (1-3): "))
        print(" Choosed: {0}".format(license_choice))
        with open("config.py", "w") as f:
            f.write(f"""
# Microbot Discord bot
# Generated 'config.py' file

import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

tokens = {{
    'discord_api': os.environ['DISCORD_TOKEN'],    # Discord API token from system environment
    'owm_api': os.environ['OPENWEATHERMAP_TOKEN']  # for OpenWeatherMap API
}}

config = {{
    'name': '{config['name']}',
    'prefix': '{config['prefix']}',
    'accent_def': {config['accent_def']},
    'accent_err': {config['accent_err']},
    'dev_id': {config['dev_id']},
    'bugs_ch': {config['bugs_ch']},
    'cooldown': {config['cooldown']},
    'license': {license_choice}
}}

links = {{
    'invite': '{links['invite'] if('invite' in links) else ''}',
    'support': '{links['support'] if('support' in links) else ''}',
    'website': '{links['website'] if('website' in links) else ''}',
    'repo': '{links['repo'] if('repo' in links) else ''}',
    'donate': '{links['donate'] if('donate' in links) else ''}'
}}
            """.replace("\t",""))
            f.close()
