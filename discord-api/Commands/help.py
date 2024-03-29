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

name = 'help'
hidden = False

async def generateEmbed(ctx, inst, config, links, version, disnake, translator):
    prefixes_list = f"`{config['prefix']}` "
    commands_list = ""
    prefixes = await inst.bot.get_prefix(ctx)

    for prefix in prefixes:
        if(prefix != config['prefix']):
            if(prefixes.index(prefix) < len(prefixes) - 1):
                prefixes_list += "`{0}`, ".format(prefix)
            else:
                prefixes_list += "`{0}`".format(prefix)
        msg_footer = ""
        if(config['name'] == 'Microbot'):
            msg_footer = translator.translate('embed_footer', 'help', inst.language).format(version['version'])
        else:
            msg_footer = translator.translate('embed_footer', 'help2', inst.language).format(version['version'])

    msg_embed = disnake.Embed(
        description=str(translator.translate('embed_description', 'help', inst.language)).format(config['name'], config['prefix'], links['invite']),
        colour=config['accent_def']
    ).add_field(
        translator.translate('embed_fields', 'help_preff', inst.language), translator.translate('embed_fields', 'help_prefv', inst.language).format(prefixes_list), inline=False
    ).set_footer(text=msg_footer).set_author(name=str(translator.translate('embed_title', 'help', inst.language)))

    for category in inst.bot.commands_list.keys():
        commands_list = ''
        for command in inst.bot.commands_list[category]:
            if(inst.bot.commands_list[category].index(command) < len(inst.bot.commands_list[category]) - 1):
                commands_list += "`{0}` ".format(command)
            else:
                commands_list += "`{0}`".format(command)
        msg_embed.add_field(
            translator.translate('command_categories', category, inst.language), commands_list, inline=False
        )
    return msg_embed

async def sendSlashMsg(ctx, inst, config, links, version, disnake, translator):
    msg_embed = await generateEmbed(ctx, inst, config, links, version, disnake, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, inst, config, links, version, disnake, translator):
    msg_embed = await generateEmbed(ctx, inst, config, links, version, disnake, translator)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendCmdHelpMsg(ctx, inst, links, config, disnake, translator, arg):
    for category in inst.bot.commands_list.keys():
        commands_result = 0
        for command in inst.bot.commands_list[category]:
            if(command == arg):
                commands_result = 1
    if(commands_result > 0):
        msg_embed = disnake.Embed(
            title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format(arg),
            description=str(translator.translate('command_description', arg, inst.language)),
            colour=config['accent_def'],
        )
        msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', inst.language), translator.translate('command_examples', arg, inst.language).format(config['prefix']), inline=False)
    else:
        if(links['repo'] == None or len(links['repo']) == 0):
            msg_embed = disnake.Embed(
                title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format(arg),
                description=str(translator.translate('embed_description', 'cmd_not_found2', inst.language)),
                colour=config['accent_err'],
            )
        else:
            msg_embed = disnake.Embed(
                title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format(arg),
                description=str(translator.translate('embed_description', 'cmd_not_found', inst.language).format(links['repo'] + "/issues")),
                colour=config['accent_err'],
            )
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendCmdHelpWithoutArgs(ctx, inst, config, disnake, translator):
    aliases = None
    custom_prefix = ''
    for prefix in await inst.bot.get_prefix(ctx.message):
        if(ctx.message.content.startswith(prefix)):
            custom_prefix = prefix
    if(ctx.message.content.startswith('{0}help'.format(config['prefix'])) or ctx.message.content.startswith('{0}help'.format(custom_prefix))):
        query = 'help'
    elif(ctx.message.content.startswith('{0}about'.format(config['prefix'])) or ctx.message.content.startswith('{0}about'.format(custom_prefix))):
        query = 'about'
        aliases = ['`state`', '`check`']
    elif(ctx.message.content.startswith('{0}state'.format(config['prefix'])) or ctx.message.content.startswith('{0}state'.format(custom_prefix))):
        query = 'about'
        aliases = ['`state`', '`check`']
    elif(ctx.message.content.startswith('{0}user'.format(config['prefix'])) or ctx.message.content.startswith('{0}user'.format(custom_prefix))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.message.content.startswith('{0}member'.format(config['prefix'])) or ctx.message.content.startswith('{0}member'.format(custom_prefix))):
        query = 'user'
        aliases = ['`member`']
    elif(ctx.message.content.startswith('{0}avatar'.format(config['prefix'])) or ctx.message.content.startswith('{0}avatar'.format(custom_prefix))):
        query = 'avatar'
    elif(ctx.message.content.startswith('{0}8ball'.format(config['prefix'])) or ctx.message.content.startswith('{0}8ball'.format(custom_prefix))):
        query = '8ball'
    elif(ctx.message.content.startswith('{0}rngen'.format(config['prefix'])) or ctx.message.content.startswith('{0}rngen'.format(custom_prefix))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.message.content.startswith('{0}rand'.format(config['prefix'])) or ctx.message.content.startswith('{0}rand'.format(custom_prefix))):
        query = 'rngen'
        aliases = ['`rand`']
    elif(ctx.message.content.startswith('{0}calc'.format(config['prefix'])) or ctx.message.content.startswith('{0}calc'.format(custom_prefix))):
        query = 'calc'
    elif(ctx.message.content.startswith('{0}guild'.format(config['prefix'])) or ctx.message.content.startswith('{0}guild'.format(custom_prefix))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.message.content.startswith('{0}server'.format(config['prefix'])) or ctx.message.content.startswith('{0}server'.format(custom_prefix))):
        query = 'guild'
        aliases = ['`server`']
    elif(ctx.message.content.startswith('{0}weather'.format(config['prefix'])) or ctx.message.content.startswith('{0}weather'.format(custom_prefix))):
        query = 'weather'
    elif(ctx.message.content.startswith('{0}wiki'.format(config['prefix'])) or ctx.message.content.startswith('{0}wiki'.format(custom_prefix))):
        query = 'wiki'
    elif(ctx.message.content.startswith('{0}publish'.format(config['prefix'])) or ctx.message.content.startswith('{0}publish'.format(custom_prefix))):
        query = 'publish'
    else:
        return
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format(query),
        description=str(translator.translate('command_description', query, inst.language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', inst.language), translator.translate('command_examples', query, inst.language).format(config['prefix']), inline=False)
    if(aliases != None):
        msg_embed.add_field(translator.translate('embed_fields', 'help_aliasf', inst.language), ' '.join(aliases), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
