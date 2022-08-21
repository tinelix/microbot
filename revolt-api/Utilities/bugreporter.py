# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

async def generateBrEmbed(ctx, bot, config, language, voltage, translator, error):
    if(ctx.message.content.startswith('{0}help'.format(config['prefix']))):
        command_example = translator.translate('command_examples', 'help', 'en_US')
    elif(ctx.message.content.startswith('{0}about'.format(config['prefix']))):
        command_example = translator.translate('command_examples', 'about', 'en_US')
    elif(ctx.message.content.startswith('{0}user'.format(config['prefix']))):
        command_example = translator.translate('command_examples', 'user', 'en_US')
    elif(ctx.message.content.startswith('{0}avatar'.format(config['prefix']))):
        command_example = translator.translate('command_examples', 'avatar', 'en_US')
    elif(ctx.message.content.startswith('{0}8ball'.format(config['prefix']))):
        command_example = translator.translate('command_examples', '8ball', 'en_US')
    elif(ctx.message.content.startswith('{0}guild'.format(config['prefix']))):
        command_example = translator.translate('command_examples', 'guild', 'en_US')
    else:
        command_example = '*Unknown*'

    msg_embed = voltage.SendableEmbed(
        title='Bug report',
        description='```{0}```'.format(error),
        colour=config['accent_err']
    )
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(
        'How to reproduce the bug?', command_example.format(config['prefix']))
    msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'about_versf', 'en_US'), translator.translate('embed_fields', 'about_versv', 'en_US').format(config['version'], config['version_date']))
    return msg_embed

async def generateEmbed(ctx, bot, config, language, voltage, translator, error):
    msg_embed = voltage.SendableEmbed(
        title=translator.translate('embed_title', 'bug_reporter', language),
        description=translator.translate('embed_description', 'bug_reporter', language),
        colour=config['accent_err']
    )
    return msg_embed

async def send(ctx, bot, config, language, voltage, translator, error):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, error)
    if(config['bugs_ch'] == ''):
        try:
            channel = bot.get_channel(config['bugs_ch'])
            msg_bug_embed = await generateBrEmbed(ctx, bot, config, language, voltage, translator, error)
            await channel.send(embed=msg_bug_embed)
        except:
            print(' BUG DETECTED!\r\n\r\n {0}\r\n\r\n How to reproduce the bug? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), config['version'], config['version_date']))
    else:
        print(' BUG DETECTED!\r\n\r\n {0}\r\n\r\n How to reproduce the bug? {1}\r\n Version: {2}\r\n\r\n'.format(error, command_example.format(config['prefix']), config['version'], config['version_date']))
    await ctx.reply(embed=msg_embed, mention_author=False)
