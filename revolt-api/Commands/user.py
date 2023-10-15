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

import re
import datetime

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    if(arg.startswith("<@") and arg.endswith(">")):
        query = "".join(arg).replace("<@", "").replace(">", "")
    else:
        query = arg
    user = bot.get_user(query)
    member = ctx.server.get_member(query)

    if(user == None):
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'error', language)),
            description=translator.translate('embed_description', 'error_unf', language),
            colour=config['accent_err'],
        )
        return await ctx.send(embed=msg_embed)
    if(member != None and member.bot == True):
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'user_bot', language)).format(user.name),
            colour=config['accent_def'],
        )
    elif user.id == ctx.server.owner_id:
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'user_owner', language)).format(user.name),
            colour=config['accent_def'],
        )
    else:
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'user', language)).format(user.name),
            colour=config['accent_def'],
        )

    if(member == None):
        nick = None
        status == None
    else:

        if(member.status.presence == voltage.PresenceType.online):
            status = translator.translate('embed_fields', 'user_statusv', language)
        elif(member.status.presence == voltage.PresenceType.idle):
            status = translator.translate('embed_fields', 'user_statusv2', language)
        elif(member.status.presence == voltage.PresenceType.busy):
            status = translator.translate('embed_fields', 'user_statusv3', language)
        else:
            status = translator.translate('embed_fields', 'user_statusv4', language)

        roles = ''

        for role in member.roles:
            if(member.roles.index(role) < int(len(member.roles) - 1)):
                roles += '{0}, '.format(str(role.name))
            else:
                roles += '{0}'.format(str(role.name))


    if(member == None):
        pass
    else:
        msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'user_statusf', language), status)
        msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'guild_crtf', language), translator.translate('embed_fields', 'guild_crtv', language).format(datetime.datetime.fromtimestamp(user.created_at / 1000).strftime("%Y-%m-%d %H:%M:%S")))
        if(len(member.roles) > 0):
            msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'user_rolesf', language).format(len(member.roles)), roles)
    msg_embed.description += '###### ID: {0}'.format(user.id)
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, voltage, translator, arg):
    if(arg.startswith("<@") and arg.endswith(">")):
        query = "".join(arg).replace("<@", "").replace(">", "")
    else:
        query = arg
    user = bot.get_user(query)
    member = ctx.server.get_member(query)
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    if(arg.startswith("<@") and arg.endswith(">")):
        query = "".join(arg).replace("<@", "").replace(">", "")
    else:
        query = arg
    user = bot.get_user(query)
    member = ctx.message.server.get_member(query)
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.reply(" ", embed=msg_embed)

async def sendHelpMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', language)),
        colour=config['accent_def'],
    )
    msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'user', language).format(config['prefix']))
    await ctx.send(embed=msg_embed)
