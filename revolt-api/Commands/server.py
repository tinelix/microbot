# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re
import datetime

async def generateEmbed(ctx, bot, config, language, voltage, translator):
    server = ctx.server
    try:
        server_pr = await bot.fetch_guild_preview(ctx.server.id)
    except:
        server_pr = None
    owner = bot.get_user(server.owner_id)

    msg_embed = voltage.SendableEmbed(
        title=ctx.server.name,
        colour=config['accent_def'],
    )
    if(server_pr == None):
        pass
    else:
        msg_embed.icon_url = server.icon

    people = 0
    bots = 0
    online = 0

    for member in server.members:
        if(member.bot == True):
            bots += 1
        else:
            people += 1
        if(str(member.status) == 'online' or str(member.status) == 'idle' or str(member.status) == 'dnd'):
            online += 1

    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'guild_ownerf', language), translator.translate('embed_fields', 'guild_ownerv', language).format(owner.name))
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'guild_crtf', language), translator.translate('embed_fields', 'guild_crtv', language).format(datetime.datetime.fromtimestamp(server.created_at[0] / 1000).strftime("%Y-%m-%d %H:%M:%S")))
    msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'guild_statsf', language), translator.translate('embed_fields', 'guild_statsv', language).format(len(server.members), people, round(people / (len(server.members) * 0.01), 2), bots, round(bots / (len(server.members) * 0.01), 2), online, round(online / (len(server.members) * 0.01), 2), 0))

    msg_embed.description += '###### ID: {0}'.format(server.id)
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator)
    await ctx.reply(" ", embed=msg_embed)

async def sendHelpMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = voltage.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', 'ru_RU')),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', 'ru_RU'), translator.translate('command_examples', 'user', 'ru_RU').format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
