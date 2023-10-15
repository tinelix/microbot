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

async def showWelcomeMessage(voltage, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' S: {3}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}'.format(bot.user.name), len(bot.cache.servers)))
    await bot.set_status("{0} servers".format(len(bot.cache.servers)), voltage.PresenceType.busy)

async def refreshStatus(voltage, bot, config):
    await bot.set_status("{0} servers".format(len(bot.cache.servers)), voltage.PresenceType.busy)

async def updateWelcomeMessage(voltage, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' S: {3}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}'.format(bot.user.name), len(bot.cache.servers)))
