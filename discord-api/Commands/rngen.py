# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import random

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    random_numb = random.randint(int(arg.split('-')[0]), int(arg.split('-')[1]))
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'rngen_numbf', language), random_numb)
    msg_embed.set_author(name=str(translator.translate('embed_title', 'rngen', language)))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg):
    try:
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
        class RetryButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'rngen_retry', language))
            async def regenerate(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
                await interaction.response.send_message(embed=msg_embed)
        await ctx.response.send_message(embed=msg_embed, view=RetryButton())
    except:
        await sendHelpMsg(ctx, bot, config, language, disnake, translator)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    try:
        if(len(arg.split('-')) == 2):
            msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
            class RetryButton(disnake.ui.View):
                @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'rngen_retry', language))
                async def regenerate(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
                    await interaction.response.send_message(embed=msg_embed, view=RetryButton())
            await ctx.reply(embed=msg_embed, view=RetryButton(), mention_author=False)
        else:
            await sendHelpMsg(ctx, bot, config, language, disnake, translator)
    except:
        await sendHelpMsg(ctx, bot, config, language, disnake, translator)

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('rngen'),
        description=str(translator.translate('command_description', 'rngen', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'rngen', language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
