import os
from dotenv import load_dotenv # loading environment variables module, for install 'pip install python-dotenv'
dotenv_path = os.path.join('../', '.env')

config = {
    'token': os.environ['TOKEN'], # Discord API token from system environment
    'name': 'Microbot',
    'version': '0.0.3',
    'version_date': '2022-07-13',
    'prefix': '>',
    'accent_def': 0x33b5e5,
    'accent_err': 0xff4444,
    'owner_id': 741883312108339231, # Bot developer ID
    'bugs_ch': 995275176029732894, # To show a bug report in the console, set the value to 0
}

links = {
    'invite': 'https://discord.com/api/oauth2/authorize?client_id=994906248526970951&permissions=2147862592&scope=bot',
    'support': 'https://discord.gg/saEHAWzYt3',
    'website': 'https://tinelix.github.io',
    'repo': 'https://github.com/tinelix/microbot',
}
