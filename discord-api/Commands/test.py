async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, fatalerr_reporter):
    if(ctx.message.author.id == config['dev_id']):  # only bot owner!
        if("fatal_err" in arg):
            error_text = "RzhachError: XD"
            if(config['bugs_ch'] > 0):
                await fatalerr_reporter.send(ctx, bot, config, language, disnake, translator, error_text, 'regular')
            else:
                print(' WE\'VE GOT SOMETHING BROKEN!\r\n{0}'.format(error_text))
    else:
        msg_embed = disnake.Embed(
            description=str(translator.translate('embed_description', 'forbidden', language)),
            colour=config['accent_err']
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
        ctx.reply(embed=msg_embed, mention_author=False)
