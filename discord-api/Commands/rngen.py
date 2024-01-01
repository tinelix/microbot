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

import random

name = 'rngen'
hidden = False

async def generateEmbed(ctx, inst, config, disnake, translator, arg):
    random_numb = random.randint(int(arg.split('-')[0]), int(arg.split('-')[1]))
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'rngen_numbf', inst.language), random_numb)
    msg_embed.set_author(name=str(translator.translate('embed_title', 'rngen', inst.language)))
    return msg_embed

async def sendSlashMsg(ctx, inst, config, disnake, translator, arg):
    try:
        msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg)
        class RetryButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'rngen_retry', inst.language))
            async def regenerate(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg)
                await interaction.response.send_message(embed=msg_embed)
        await ctx.response.send_message(embed=msg_embed, view=RetryButton())
    except:
        await sendHelpMsg(ctx, inst, config, language, disnake, translator)

async def sendRegularMsg(ctx, inst, config, disnake, translator, arg):
    try:
        if(len(arg.split('-')) == 2):
            msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg)
            class RetryButton(disnake.ui.View):
                @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'rngen_retry', inst.language))
                async def regenerate(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                    msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg)
                    await interaction.response.send_message(embed=msg_embed, view=RetryButton())
            await ctx.reply(embed=msg_embed, view=RetryButton(), mention_author=False)
        else:
            await sendHelpMsg(ctx, inst, config, disnake, translator)
    except:
        await sendHelpMsg(ctx, inst, config, disnake, translator)

async def sendHelpMsg(ctx, inst, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format('rngen'),
        description=str(translator.translate('command_description', 'rngen', inst.language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', inst.language), translator.translate('command_examples', 'rngen', inst.language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
