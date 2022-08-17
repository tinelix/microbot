async def generateEmbed(ctx, bot, config, links, language, disnake, translator):
    msg_embed = disnake.Embed(
        description=str(translator.translate('embed_description', 'help', language)).format(config['name'], links['invite']),
        colour=config['accent_def']
    ).add_field(
        translator.translate('embed_fields', 'help_preff', language), translator.translate('embed_fields', 'help_prefv', language), inline=False
    ).add_field(
        translator.translate('embed_fields', 'help_cmdsf', language), translator.translate('embed_fields', 'help_cmdsv', language), inline=False
    )
    msg_embed.set_author(name=str(translator.translate('embed_title', 'help', language)))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, links, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, links, language, disnake, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, links, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, links, language, disnake, translator)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendCmdHelpMsg(ctx, bot, links, config, language, disnake, translator, arg):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format(arg),
        description=str(translator.translate('command_description', arg, language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', arg, language).format(config['prefix']), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendCmdHelpWithoutArgs(ctx, bot, config, language, disnake, translator):
    aliases = None
    if(ctx.message.content.startswith('{0}help'.format(config['prefix']))):
        query = 'help'
    elif(ctx.message.content.startswith('{0}about'.format(config['prefix']))):
        query = 'about'
        aliases = ['`state`', '`check`']
    elif(ctx.message.content.startswith('{0}user'.format(config['prefix']))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.message.content.startswith('{0}member'.format(config['prefix']))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.message.content.startswith('{0}avatar'.format(config['prefix']))):
        query = 'avatar'
    elif(ctx.message.content.startswith('{0}8ball'.format(config['prefix']))):
        query = '8ball'
    elif(ctx.message.content.startswith('{0}rngen'.format(config['prefix']))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.message.content.startswith('{0}rand'.format(config['prefix']))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.message.content.startswith('{0}calc'.format(config['prefix']))):
        query = 'calc'
    elif(ctx.message.content.startswith('{0}guild'.format(config['prefix']))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.message.content.startswith('{0}server'.format(config['prefix']))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.message.content.startswith('{0}weather'.format(config['prefix']))):
        query = 'weather'
    elif(ctx.message.content.startswith('{0}wiki'.format(config['prefix']))):
        query = 'wiki'
    else:
        return
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format(query),
        description=str(translator.translate('command_description', query, language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', query, language).format(config['prefix']), inline=False)
    if(aliases != None):
        msg_embed.add_field(translator.translate('embed_fields', 'help_aliasf', language), ' '.join(aliases), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
