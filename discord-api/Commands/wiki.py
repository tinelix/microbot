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

import re
import wikipedia
import urllib

name = 'wiki'
hidden = False

async def generateEmbed(ctx, inst, config, language, disnake, translator, arg):
        if(language == "ru_RU"):
            wikipedia.set_lang("ru")
        else:
            wikipedia.set_lang("en")
        try:
            search_results = wikipedia.search(arg)
            article = search_results[0]
            if(len(search_results) > 0):
                page = wikipedia.page(article)
                full_content = page.content.replace('_', '\_').replace('`', '\`').replace('*', '\*').replace('~', '\~').replace('|', '\|').replace('>', '\>')
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
                msg_embed.set_author(name=str(translator.translate('embed_title', 'wikipedia', inst.language)))
            else:
                msg_embed = disnake.Embed(
                    colour=config['accent_err'],
                    description=translator.translate('embed_description', 'query_notfound', inst.language)
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'error', inst.language)))
        except Exception as e:
            print(" ERROR: {0}".format(e))
            msg_embed = disnake.Embed(
                colour=config['accent_err'],
                description=translator.translate('embed_description', 'query_notfound', inst.language)
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'error', inst.language)))
        return msg_embed

async def sendSlashMsg(ctx, inst, config, disnake, translator, arg):
    await ctx.response.defer()
    msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg)
    await ctx.send(embed=msg_embed)

async def sendRegularMsg(ctx, inst, config, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, inst, config,  disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, bot, config, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('wiki'),
        description=str(translator.translate('command_description', 'wiki', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'wiki', language).format(config['prefix']), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
