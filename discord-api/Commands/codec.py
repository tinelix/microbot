#   Tinelix Microbot
#   -------------------------------------------------------------------------------------------
#   Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
#   This program is free software: you can redistribute it and/or modify it under the terms of
#   the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
#   See the following files in this directory for the precise terms and conditions of either
#   license:
#
#       LICENSE.APACHE
#       LICENSE.AGPL
#
#   Please see each file in the implementation for copyright and licensing
#   information, (in the opening comment of each file).

import base64
import binascii

name = 'codec'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg, binary):
    msg_embed = None
    result = None
    if(len(arg) >= 2):
        if(arg[0] == '-d'):
            if(arg[1] == 'base64'):
                algoritm = "Base64 (Standard)"
                try:
                    result = base64.standard_b64decode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_derrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            elif(arg[1] == 'base32'):
                algoritm = "Base32"
                try:
                    result = base64.b32decode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_derrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            elif(arg[1] == 'base16'):
                algoritm = "Base16"
                try:
                    result = base64.b16decode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_derrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
            elif(arg[1] == 'binary'):
                algoritm = translator.translate('embed_fields', 'codec_algv2', language)
                try:
                    result = str(binary.decode(" ".join(arg[2:])))
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except Exception as e:
                    print(e)
                    result = translator.translate('embed_fields', 'codec_derrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
        elif(arg[0] == '-e'):
            if(arg[1] == 'base64'):
                algoritm = "Base64 (Standard)"
                try:
                    result = base64.standard_b64encode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_eerrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            elif(arg[1] == 'base32'):
                algoritm = "Base32"
                try:
                    result = base64.b32encode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_eerrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            elif(arg[1] == 'base16'):
                algoritm = "Base16"
                try:
                    result = base64.b16encode(" ".join(arg[2:]).encode('ascii')).decode('ascii')
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except:
                    result = translator.translate('embed_fields', 'codec_eerrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            elif(arg[1] == 'binary'):
                algoritm = translator.translate('embed_fields', 'codec_algv2', language)
                try:
                    arg_str = " ".join(arg[2:])
                    result = ""
                    for letter in list(arg_str):
                        try:
                            result += binary.encode()[letter]
                        except Exception as e:
                            print(e)
                            result += '[?]'
                    msg_embed = disnake.Embed(
                        colour=config['accent_def']
                    )
                except Exception as e:
                    print(e)
                    result = translator.translate('embed_fields', 'codec_eerrv', language)
                    msg_embed = disnake.Embed(
                        colour=config['accent_err']
                    )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'codec', language)))
                msg_embed.add_field(translator.translate('embed_fields', 'codec_resulf', language), translator.translate('embed_fields', 'codec_resulv', language).format(result), inline=False)
                msg_embed.add_field(translator.translate('embed_fields', 'codec_algf', language), translator.translate('embed_fields', 'codec_algv', language).format(algoritm), inline=False)
            else:
                await sendHelpMsg(ctx, bot, config, language, disnake, translator)
        else:
            await sendHelpMsg(ctx, bot, config, language, disnake, translator)
    else:
        await sendHelpMsg(ctx, bot, config, language, disnake, translator)
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, binary):
    try:
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, binary)
        await ctx.reply(embed=msg_embed, mention_author=False)
    except:
        pass

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, encode, decode, text, binary):
    try:
        await ctx.response.defer()
        arg = [""]
        if(encode != ""):
            arg = str("-e " + encode + " " + text).split(" ")
        elif(decode != ""):
            arg = str("-d " + decode + " " + text).split(" ")
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, binary)
        await ctx.reply(embed=msg_embed)
    except:
        pass

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('codec'),
        description=str(translator.translate('command_description', 'codec', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', 'ru_RU'), translator.translate('command_examples', 'codec', language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
