import random
import time

async def generateEmbed(ctx, bot, config, language, disnake, translator, ping):
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.set_author(name=str(translator.translate('embed_title', 'ping', language)))
    if(ping > 0):
        msg_embed.add_field(translator.translate('embed_fields', 'ping_statisticsf', language), translator.translate('embed_fields', 'ping_statisticsv2', language).format(round(bot.latency * 1000), round(ping)))
    else:
        msg_embed.add_field(translator.translate('embed_fields', 'ping_statisticsf', language), translator.translate('embed_fields', 'ping_statisticsv', language).format(round(bot.latency * 1000)))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, 0)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator):
    before = time.monotonic()
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, 0)
    msg = await ctx.reply(embed=msg_embed, mention_author=False)
    # getting execution time
    ping = (time.monotonic() - before) * 1000
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, ping)
    await msg.edit(embed=msg_embed)
