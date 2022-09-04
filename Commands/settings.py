# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import numexpr

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg, db, database, cursor):
    if(len(arg) >= 2):
        if(arg[0] == '-L' and (arg[1] == 'en_US' or arg[1] == 'ru_RU')):
            if ctx.author.guild_permissions.administrator:
                await db.update_value(ctx, database, cursor, 'guilds', 'language', '\'{0}\''.format(arg[1]), ctx.message.guild.id)
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'settings_done', arg[1])),
                    colour=config['accent_def']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', arg[1])))
            else:
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'forbidden', language)),
                    colour=config['accent_err']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
        elif(arg[0] == '-P'):
            if ctx.author.guild_permissions.administrator:
                await db.update_value(ctx, database, cursor, 'guilds', 'prefix', '\'{0}\''.format(arg[1]), ctx.message.guild.id)
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'settings_done', language)),
                    colour=config['accent_def']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            else:
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'forbidden', language)),
                    colour=config['accent_err']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
        else:
            msg_embed = disnake.Embed(
            description=str(translator.translate('embed_description', 'settings', language)),
            colour=config['accent_def'],
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            msg_embed.add_field(translator.translate('embed_fields', 'settings_availoptf', language), translator.translate('embed_fields', 'settings_availoptv', language), inline=False)
    else:
        msg_embed = disnake.Embed(
            description=str(translator.translate('embed_description', 'settings', language)),
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
        msg_embed.add_field(translator.translate('embed_fields', 'settings_availoptf', language), translator.translate('embed_fields', 'settings_availoptv', language), inline=False)
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, db, database, cursor)
    class SettingsByButton(disnake.ui.View):
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🚩')
        async def show_changing_language_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'settings_lang', language).format(config['prefix']), inline=False)
            await interaction.response.send_message(embed=language_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🪄')
        async def show_changing_prefix_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'settings_prefix', language).format(config['prefix']), inline=False)
            await interaction.response.send_message(embed=language_embed)
    if(len(arg) >= 2):
        if(arg[0] == '-L' and (arg[1] == 'en_US' or arg[1] == 'ru_RU')):
            await ctx.reply(embed=msg_embed, mention_author=False)
        elif(arg[0] == '-P'):
            await ctx.reply(embed=msg_embed, mention_author=False)
        else:
            await ctx.reply(embed=msg_embed, view=SettingsByButton(), mention_author=False)
    else:
        await ctx.reply(embed=msg_embed, view=SettingsByButton(), mention_author=False)

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, db, database, cursor)
    await ctx.send(embed=msg_embed)
