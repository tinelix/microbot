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

async def showCommandExample(config, msg_type, translator):
    if(msg_type == 'regular'):
        if(ctx.message.content.startswith('{0}help'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'help', 'en_US')
        elif(ctx.message.content.startswith('{0}about'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'about', 'en_US')
        elif(ctx.message.content.startswith('{0}user'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'user', 'en_US')
        elif(ctx.message.content.startswith('{0}avatar'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'avatar', 'en_US')
        elif(ctx.message.content.startswith('{0}calc'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'calc', 'en_US')
        elif(ctx.message.content.startswith('{0}8ball'.format(config['prefix']))):
            command_example = translator.translate('command_examples', '8ball', 'en_US')
        elif(ctx.message.content.startswith('{0}guild'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'guild', 'en_US')
        elif(ctx.message.content.startswith('{0}member'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'member', 'en_US')
        elif(ctx.message.content.startswith('{0}wiki'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'wiki', 'en_US')
        elif(ctx.message.content.startswith('{0}weather'.format(config['prefix']))):
            command_example = translator.translate('command_examples', 'weather', 'en_US')
        else:
            command_example = '*Unknown*'
    elif(msg_type == 'slash'):
        command_example = '```/{0}```'.format(ctx.application_command.name)

async def generateBrEmbed(ctx, inst, config, version, disnake, translator, error, msg_type, command_example):
    msg_embed = disnake.Embed(
        title='Fatal error report',
        description='```{0}```'.format(error),
        colour=config['accent_err']
    ).add_field(
        'How to reproduce the fatal error?', command_example.format(config['prefix']), inline=False
    ).add_field(
        translator.translate('embed_fields', 'about_versf', 'en_US'), translator.translate('embed_fields', 'about_versv', 'en_US').format(version['version'], version['version_date']), inline=False
    )
    return msg_embed

async def generateEmbed(ctx, inst, config, version, disnake, translator, error):
    msg_embed = disnake.Embed(
        description=translator.translate('embed_description', 'fatalerr_reporter', inst.language),
        colour=config['accent_err']
    )
    msg_embed.set_author(name=translator.translate('embed_title', 'fatalerr_reporter', inst.language))
    return msg_embed

async def send(ctx, inst, config, version, disnake, translator, error, msg_type):
    msg_embed = await generateEmbed(ctx, inst, config, version, disnake, translator, error)
    command_example = await showCommandExample(config, msg_type, translator);
    if(config['bugs_ch'] > 0):
        try:
            channel = bot.get_channel(config['bugs_ch'])
            msg_bug_embed = await generateBrEmbed(ctx, inst, config, version, disnake, translator, error, msg_type, command_example)
            await channel.send(embed=msg_bug_embed)
        except:
            print(' WE\'VE GOT SOMETHING BROKEN!\r\n\r\n {0}\r\n\r\n How to reproduce the fatal error? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), version['version'], version['version_date']))
    else:
        print(' WE\'VE GOT SOMETHING BROKEN!\r\n\r\n {0}\r\n\r\n How to reproduce the fatal error? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), version['version'], version['version_date']))
    if(msg_type == 'regular'):
        await ctx.reply(embed=msg_embed, mention_author=False)
    elif(msg_type == 'slash'):
       await ctx.send(embed=msg_embed)
