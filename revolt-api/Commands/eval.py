# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import platform

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    if(ctx.message.author.id == config['dev_id']):  # only bot owner!
        msg_embed = voltage.SendableEmbed(
            str(translator.translate('embed_title', 'eval', language)),
            colour=config['accent_def'],
        )
        if(arg == 'guilds'): # server list for statistical data
            eval_r = ''
            for server in bot.servers:
                online = 0
                for member in server.members:
                    if(member.status.presence == voltage.PresenceType.online or member.status.presence == voltage.PresenceType.idle or member.status.presence == voltage.PresenceType.busy):
                        online += 1
                eval_r += '{0:03d}. {1}\r\n└────┤ {2: 4d} members │ {3: 4d} online │\r\n'.format(bot.servers.index(server) + 1, server.name, len(server.members), online)

        else:
            if(len(str(eval(arg))) > 1000):
                eval_r = 'Content is too large (> 1000 symbols)'
            else:
                eval_r = str(eval(arg))
        if(arg == 'guilds'):
            pass
        else:
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_codelf', language), '``\r\n{0}\r\n``'.format(arg))
        if(msg_embed.description == None):
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_resulf', language), '```\r\n{0}\r\n```'.format(eval_r))
        else:
            msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_resulf', language), '```\r\n{0}\r\n```'.format(eval_r))
    else:
        msg_embed = msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'forbidden', language)),
            description=str(translator.translate('embed_description', 'forbidden', language)),
            colour=config['accent_err']
        )
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.reply(" ", embed=msg_embed)
