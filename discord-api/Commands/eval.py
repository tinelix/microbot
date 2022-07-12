import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import platform

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    if(ctx.message.author.id == config['owner_id']):
        msg_embed = disnake.Embed(
            title=str(translator.translate('embed_title', 'eval', language)),
            colour=config['accent_def'],
        )
        if(len(str(eval(arg))) > 1000):
            eval_r = 'Content is too large (> 1000 symbols)'
        else:
            eval_r = str(eval(arg))
        msg_embed.add_field(translator.translate('embed_fields', 'eval_codelf', language), '```py\r\n{0}```'.format(arg), inline=False)
        msg_embed.add_field(translator.translate('embed_fields', 'eval_resulf', language), '```py\r\n{0}```'.format(eval_r), inline=False)
    else:
        msg_embed = disnake.Embed(
            title=str(translator.translate('embed_title', 'forbidden', language)),
            description=str(translator.translate('embed_description', 'forbidden', language)),
            colour=config['accent_err']
        )
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)
