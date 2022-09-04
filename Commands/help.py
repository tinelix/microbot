# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Repo: https://github.com/den4ikbot/den4ikbot
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher.

async def generateEmbed(ctx, bot, config, links, language, disnake, translator):
    prefixes_list = f"`{config['prefix']}` "
    commands_list = ""
    prefixes = await bot.get_prefix(ctx)

    for prefix in prefixes:
        if(prefix != config['prefix']):
            if(prefixes.index(prefix) < len(prefixes) - 1):
                prefixes_list += "`{0}`, ".format(prefix)
            else:
                prefixes_list += "`{0}`".format(prefix)

    msg_embed = disnake.Embed(
        description=str(translator.translate('embed_description', 'help', language)).format(config['name'], links['invite']),
        colour=config['accent_def']
    ).add_field(
        translator.translate('embed_fields', 'help_preff', language), translator.translate('embed_fields', 'help_prefv', language).format(prefixes_list), inline=False
    ).set_footer(text=translator.translate('embed_footer', 'help', language).format(config['version'])).set_author(name=str(translator.translate('embed_title', 'help', language)))

    for category in bot.commands_list.keys():
        commands_list = ''
        for command in bot.commands_list[category]:
            if(bot.commands_list[category].index(command) < len(bot.commands_list[category]) - 1):
                commands_list += "`{0}` ".format(command)
            else:
                commands_list += "`{0}`".format(command)
        msg_embed.add_field(
            translator.translate('command_categories', category, language), commands_list, inline=False
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
