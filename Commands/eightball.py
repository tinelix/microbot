import random

async def generateEmbed(ctx, bot, config, language, disnake, translator, python_version):
    random_numb = random.randint(0, len(translator.translate('embed_fields', '8ball_answv', language)) - 1)
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.set_author(name=str(translator.translate('embed_title', '8ball', language)))
    msg_embed.add_field(translator.translate('embed_fields', '8ball_answf', language), translator.translate('embed_fields', '8ball_answv', language)[random_numb])
    msg_embed.set_footer(text=translator.translate('embed_footer', '8ball', language))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, python_version):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, python_version)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, python_version):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, python_version)
    await ctx.reply(embed=msg_embed, mention_author=False)
