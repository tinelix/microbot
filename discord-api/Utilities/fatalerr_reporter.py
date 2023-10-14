# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

async def generateBrEmbed(ctx, bot, config, language, disnake, translator, error, msg_type):
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

    msg_embed = disnake.Embed(
        title='Fatal error report',
        description='```{0}```'.format(error),
        colour=config['accent_err']
    ).add_field(
        'How to reproduce the fatal error?', command_example.format(config['prefix']), inline=False
    ).add_field(
        translator.translate('embed_fields', 'about_versf', 'en_US'), translator.translate('embed_fields', 'about_versv', 'en_US').format(config['version'], config['version_date']), inline=False
    )
    return msg_embed

async def generateEmbed(ctx, bot, config, language, disnake, translator, error):
    msg_embed = disnake.Embed(
        description=translator.translate('embed_description', 'fatalerr_reporter', language),
        colour=config['accent_err']
    )
    msg_embed.set_author(name=translator.translate('embed_title', 'fatalerr_reporter', language))
    return msg_embed

async def send(ctx, bot, config, language, disnake, translator, error, msg_type):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, error)
    if(config['bugs_ch'] > 0):
        try:
            channel = bot.get_channel(config['bugs_ch'])
            msg_bug_embed = await generateBrEmbed(ctx, bot, config, language, disnake, translator, error, msg_type)
            await channel.send(embed=msg_bug_embed)
        except:
            print(' WE\'VE GOT SOMETHING BROKEN!\r\n\r\n {0}\r\n\r\n How to reproduce the fatal error? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), config['version'], config['version_date']))
    else:
        print(' WE\'VE GOT SOMETHING BROKEN!\r\n\r\n {0}\r\n\r\n How to reproduce the fatal error? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), config['version'], config['version_date']))
    if(msg_type == 'regular'):
        await ctx.reply(embed=msg_embed, mention_author=False)
    elif(msg_type == 'slash'):
       await ctx.send(embed=msg_embed)