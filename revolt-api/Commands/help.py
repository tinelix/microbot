# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

async def generateEmbed(ctx, bot, config, links, language, voltage, translator):
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'help', language)),
        description="{0}".format(str(translator.translate('embed_description', 'help', language)).format(config['name'], links['invite'])),
        colour=config['accent_def']
    )
    if(msg_embed.description != None):
        msg_embed.description += "\r\n### {0}\r\n{1}\r\n### {2}\r\n{3}".format(
            translator.translate('embed_fields', 'help_preff', language),
            translator.translate('embed_fields', 'help_prefv', language),
            translator.translate('embed_fields', 'help_cmdsf', language),
            translator.translate('embed_fields', 'help_cmdsv', language)
        )
    return msg_embed

async def sendSlashMsg(ctx, bot, config, links, language, voltage, translator):
    msg_embed = await generateEmbed(ctx, bot, config, links, language, voltage, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, links, language, voltage, translator):
    msg_embed = await generateEmbed(ctx, bot, config, links, language, voltage, translator)
    await ctx.reply(" ", embed=msg_embed)

async def sendCmdHelpMsg(ctx, bot, links, config, language, voltage, translator, arg):
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format(arg),
        description="{0}\r\n### {1}\r\n{2}".format(str(translator.translate('command_description', arg, language)), translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', arg, language).format(config['prefix'])),
        colour=config['accent_def'],
    )
    await ctx.reply(" ", embed=msg_embed)

async def sendCmdHelpWithoutArgs(ctx, bot, config, language, voltage, translator):
    aliases = None
    if(ctx.content.startswith('{0}help'.format(config['prefix']))):
        query = 'help'
    elif(ctx.content.startswith('{0}about'.format(config['prefix']))):
        query = 'about'
        aliases = ['`state`', '`check`']
    elif(ctx.content.startswith('{0}user'.format(config['prefix']))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.content.startswith('{0}member'.format(config['prefix']))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.content.startswith('{0}avatar'.format(config['prefix']))):
        query = 'avatar'
    elif(ctx.content.startswith('{0}8ball'.format(config['prefix']))):
        query = '8ball'
    elif(ctx.content.startswith('{0}rngen'.format(config['prefix']))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.content.startswith('{0}rand'.format(config['prefix']))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.content.startswith('{0}calc'.format(config['prefix']))):
        query = 'calc'
    elif(ctx.content.startswith('{0}guild'.format(config['prefix']))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.content.startswith('{0}server'.format(config['prefix']))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.content.startswith('{0}weather'.format(config['prefix']))):
        query = 'weather'
    elif(ctx.content.startswith('{0}wiki'.format(config['prefix']))):
        query = 'wiki'
    else:
        return
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format(query),
        description=str(translator.translate('command_description', query, language)),
        colour=config['accent_def'],
    )
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', query, language).format(config['prefix']))
    if(aliases != None):
        msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'help_aliasf', language), ' '.join(aliases))
    await ctx.reply(" ", embed=msg_embed)
