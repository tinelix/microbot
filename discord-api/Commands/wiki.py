# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re
import wikipedia

name = 'wiki'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
        if(language == "ru_RU"):
            wikipedia.set_lang("ru")
        else:
            wikipedia.set_lang("en")
        try:
            search_results = wikipedia.search(arg)
            article = search_results[0]
            if(len(search_results) > 0):
                page = wikipedia.page(article)
                full_content = page.content
                short_content_split = full_content.split(' ', 159)
                if(len(full_content.split(' ')) > 160):
                    short_content = " ".join(short_content_split[0:159]) + "..."
                else:
                    short_content = " ".join(short_content_split[0:159])
                msg_embed = disnake.Embed(
                    title=page.title,
                    url=page.url,
                    colour=config['accent_def'],
                    description=translator.translate('embed_description', 'wikipedia', language).format(short_content, page.url)
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'wikipedia', language)))
            else:
                msg_embed = disnake.Embed(
                    colour=config['accent_err'],
                    description=translator.translate('embed_description', 'query_notfound', language)
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
        except:
            print(" ERROR: Internal Wikipedia error")
            msg_embed = disnake.Embed(
                colour=config['accent_err'],
                description=translator.translate('embed_description', 'query_notfound', language)
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
        return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg):
    await ctx.response.defer()
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.send(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('wiki'),
        description=str(translator.translate('command_description', 'wiki', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'wiki', language).format(config['prefix']), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
