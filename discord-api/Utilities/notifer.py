import os

async def showWelcomeMessage(disnake, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' L: {3} ms │ G: {4}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}#{1}'.format(bot.user.name, bot.user.discriminator), round(bot.latency * 1000, 2), len(bot.guilds)))
    game = disnake.Game("{0} guilds".format(len(bot.guilds)), type=disnake.ActivityType.watching)
    await bot.change_presence(status=disnake.Status.dnd, activity=game)

async def refreshStatus(disnake, bot, config):
    game = disnake.Game("{0} guilds".format(len(bot.guilds)), type=disnake.ActivityType.watching)
    await bot.change_presence(status=disnake.Status.dnd, activity=game)

async def updateWelcomeMessage(disnake, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' L: {3} ms │ G: {4}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}#{1}'.format(bot.user.name, bot.user.discriminator), round(bot.latency * 1000, 2), len(bot.guilds)))
