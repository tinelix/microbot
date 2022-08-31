# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Repo: https://github.com/den4ikbot/den4ikbot
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher.

def translate(where, str, language):
    try:
        if language == "ru_RU": # Russian
            if where == "embed_title":
                locale = {
                    'error': '❎ Ошибка',
                    'help': '❔ Справка',
                    'cmd_help': 'Команда `{0}`',
                    'bug_reporter': '🪲 Баг обнаружен!',
                    'about': '🤖 О боте',
                    'user': '👤 {0}#{1}',
                    'user_bot': '🤖 {0}#{1}',
                    'user_owner': '👑 {0}#{1}',
                    'avatar': '🖼 Аватар пользователя {0}#{1}',
                    'forbidden': '🚫 Доступ запрещен',
                    'eval': '⌨ Интерпретатор',
                    '8ball': '🎱 Генератор случайных ответов',
                    'rngen': '🎱 Генератор случайных чисел',
                    'calc': '🔢 Калькулятор',
                    'ping': '🏓 Понг!',
                    'settings': '⚙ Настройки',
                }
            elif where == "embed_description":
                locale = {
                    'help': '{0} - простейший и компактный бот для Discord. На базе [Microbot](https://github.com/tinelix/microbot) от Tinelix.\r\n[Пригласить]({1})',
                    'error_unf': '😔 Пользователь не найден. Попробуйте найти другого пользователя.',
                    'bug_reporter': '🪲 Да, у нас и такое случается. Но ничего страшного, сейчас отправим разработчикам на исправление этого бага.',
                    'forbidden': '🚫 Вы не имеете права пользоваться этой командой!',
                    'please_wait': '⌛ Подождите...',
                    'settings': '**Настройки сервера:** 🇷🇺',
                    'settings_done': '✅ Готово!',
                    'query_notfound': '😔 К сожалению, мы ничего не нашли. Может, попробуете другой запрос?',
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Префиксы',
                    'help_prefv': '{0} или `/`',
                    'help_cmdsf': 'Команды',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Пример',
                    'help_aliasf': 'Аналогичные названия',
                    'eval_codelf': 'Листинг',
                    'eval_resulf': 'Результат',
                    'about_versf': 'Версия',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Разработчик',
                    'about_devsf2': 'Разработчики',
                    'about_devsv': '`{0}#{1}`',
                    'about_devsv2': '`{0}#{1}` и `{2}#{3}`',
                    'about_regdf': 'Дата регистрации',
                    'about_regdv': '{0}',
                    'about_statsf': 'Статистика',
                    'about_statsv': '{0} серверов\r\n{1} пользователей',
                    'about_uptimef': 'Активен',
                    'about_uptimev': '{0}',
                    'about_basedf': 'Работает на базе',
                    'about_basedv': 'Python {0}\r\nDisnake {1}\r\nSQLite {2}',
                    'about_hardwf': 'Оборудование',
                    'about_hardwv': '**ЦП:** {0} ({1} МГц)\r\n**ОЗУ:** {2}\r\n**Платформа:** {3}',
                    'about_linksf': 'Ссылки',
                    'about_linksv': '[Пригласить]({0})',
                    'about_linksv2': '[Сайт]({0})',
                    'about_linksv3': '[Исходный код]({0}) (Apache License 2.0 & AGPL 3.0+)',
                    'about_linksv4': '[Сервер поддержки]({0})',
                    'about_linksv5': '[YouTube-канал]({0})',
                    'user_nickf': 'Псевдоним',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Отсутствует*',
                    'user_regdf': 'Дата регистрации',
                    'user_regdv': '{0}',
                    'user_joinf': 'Дата входа на сервер',
                    'user_joinv': '{0}',
                    'user_statusf': 'Статус',
                    'user_statusv': '<:online:1012294415731146765> Онлайн',
                    'user_statusv2': '<:idle:1012294411020947457> Отошел',
                    'user_statusv3': '<:dnd:1012294408412082186> Не беспокоить',
                    'user_statusv4': '<:offline:1012294452246753300> Оффлайн',
                    'user_rolesf': 'Роли ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Владелец',
                    'guild_ownerv': '{0} (`{1}#{2}`)',
                    'guild_crtf': 'Дата создания',
                    'guild_crtv': '{0}',
                    'guild_blvlf': 'Уровень бустов',
                    'guild_blvlv': 'Уровень {0}',
                    'guild_mlvlf': 'Степень модерации',
                    'guild_mlvlv': 'Без ограничений',
                    'guild_mlvlv2': 'Только подтвержденный e-mail',
                    'guild_mlvlv3': 'Регистрация более 5 минут',
                    'guild_mlvlv4': 'Присутствие более 10 минут',
                    'guild_mlvlv5': 'Только подтвержденный телефон',
                    'guild_statsf': 'Статистика',
                    'guild_statsv': '**Всего {0} участников**\r\n👤 {1} ({2}%)\r\n🤖 {3} ({4}%)\r\n<:online:1012294415731146765> {5} ({6}%)\r\n<:channels:1012296573364998196> {7}',
                    'guild_rulesf': 'Правила',
                    'guild_rulesv': '{0}',
                    'guild_featurf': 'Функции',
                    'guild_featurv': 'Автомодерация',
                    'guild_featurv2': 'Сообщество',
                    'guild_featurv3': 'Новости',
                    'guild_featurv4': 'Чаты в голосовых каналах',
                    'guild_featurv5': 'Экран приветствия',
                    '8ball_answf': 'Ответ',
                    '8ball_answv': ['Да.', 'Нет.', 'Возможно.', 'Может быть.', 'Время покажет.', 'Поживем - увидим.', 'Навряд ли.', 'Конечно.', 'Да-да.', 'Неа.', 'Так и есть.', 'Понятия не имею.', 'Я не знаю.', 'Я хз.', 'Без понятия.', 'Наверное, да...', 'Наверное, нет...', 'Да фиг знает!', 'Я не понял ваш вопрос, можете повторить?', 'Попробуйте задать другой вопрос. Может быть, я что-то не понимаю?', 'Вероятно.', 'Ничего подобного.'],
                    'rngen_numbf': 'Число',
                    'rngen_numbv': '{0}',
                    'calc_resulf': 'Результат',
                    'calc_rlerrv': 'ОШИБКА: Попытка деления на ноль',
                    'calc_rlerrv2': 'ОШИБКА: Слишком большое число',
                    'calc_rlerrv3': 'ОШИБКА: Принимаются только числа',
                    'calc_rlerrv4': 'ОШИБКА: {0}',
                    'calc_asignf': 'Доступные знаки',
                    'calc_asignv': '[`+`] - сложение\r\n[`-`] - удаление\r\n[`/`], [`:`] - деление\r\n[`*`] - умножение',
                    'ping_statisticsf': 'Статистика',
                    'ping_statisticsv': '**Задержка:** {0} мсек',
                    'ping_statisticsv2': '**Задержка:** {0} мсек\r\n**Время выполнения:** {1} мсек',
                    'settings_availoptf': 'Доступные параметры',
                    'settings_availoptv': '🚩 Язык (Language)\r\n🪄 Префикс',
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'Все совпадения случайны!'
                }
            elif where == "command_description":
                locale = {
                    'help': 'Показывает справочную информацию, включая список доступных команд.',
                    'about': 'Показывает описание бота, а также служебную информацию.',
                    'user': 'Показывает информацию о пользователе.',
                    'avatar': 'Показывает аватарки пользователя.',
                    '8ball': 'Генерирует для любого вопроса случайный ответ. Все совпадения случайны!',
                    'rngen': 'Генерирует случайное число в указанном диапазоне.',
                    'guild': 'Показывает информацию о гильдии (сервере)',
                    'calc': 'Простейший калькулятор.',
                    'ping': 'Пни меня.',
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@упоминание или ID участника]```',
                    'avatar': '```{0}avatar [@упоминание или ID участника]```',
                    '8ball': '```{0}8ball [вопрос]```',
                    'rngen': '```{0}rngen [начало диапазона]-[конец диапазона]```',
                    'guild': '```{0}guild```',
                    'ping': '```{0}ping```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L ru_RU```',
                    'settings_prefix': '```{0}settings -P m!```',
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Показать аватар',
                    'rngen_retry': 'Повторить',
                }
            elif where == "numb_with_unit":
                locale = {
                    'bytes': '{0} байт',
                    'bytes2': '{0} / {1} байт',
                    'kilobytes': '{0} кБ',
                    'kilobytes2': '{0} / {1} кБ',
                    'megabytes': '{0} МБ',
                    'megabytes2': '{0} / {1} МБ',
                    'gigabytes': '{0} ГБ',
                    'gigabytes2': '{0} / {1} ГБ',
                }
            else:
                locale = {
                }
            if len(locale) == 0: # if string not found (variant #1)
                return "[{0}|{1}] Строка не найдена".format(str, where)
            else:
                return locale[str]
        else: # English, if not
            if where == "embed_title":
                locale = {
                    'error': '❎ Error',
                    'help': '❔ Help',
                    'cmd_help': '`{0}` command',
                    'about': '❔ About',
                    'user': '👤 {0}#{1}',
                    'user_bot': '🤖 {0}#{1}',
                    'user_owner': '👑 {0}#{1}',
                    'avatar': '🖼 {0}#{1}\'s avatar',
                    'bug_reporter': '🪲 Bug detected!',
                    'forbidden': '🚫 Access forbidden',
                    'eval': '⌨ Interpreter',
                    'calc': '🔢 Calculator',
                    'ping': '🏓 Pong!',
                    'settings': '⚙ Settings',
                }
            elif where == "embed_description":
                locale = {
                    'help': '{0} - is a simple and compact bot for Discord. Based on [Microbot](https://github.com/tinelix/microbot) by Tinelix\r\n[Invite]({1})',
                    'error_unf': '😔 User not found. Try to find another user.',
                    'bug_reporter': '🪲 Yep, this happens to us too. But it\'s okay, now we\'ll send it to the developers to fix this bug.',
                    'forbidden': '🚫 You do not have the right to use this command!',
                    'please_wait': '⌛ Wait...',
                    'settings': '**Server settings:** 🇺🇸 | {0}',
                    'settings_done': '✅ Done!',
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Prefixes',
                    'help_prefv': '{0} or `/`',
                    'help_cmdsf': 'Commands',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Examples',
                    'help_aliasf': 'Aliases',
                    'eval_codelf': 'Code listing',
                    'eval_resulf': 'Result',
                    'about_versf': 'Version',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Developer',
                    'about_devsf2': 'Developers',
                    'about_devsv': '`{0}#{1}`',
                    'about_devsv2': '`{0}#{1}` and `{2}#{3}`',
                    'about_regdf': 'Registration date',
                    'about_regdv': '{0}',
                    'about_statsf': 'Statistics',
                    'about_statsv': '{0} servers\r\n{0} users',
                    'about_uptimef': 'Uptime',
                    'about_uptimev': '{0}',
                    'about_basedf': 'Powered by',
                    'about_basedv': 'Python {0}\r\nDisnake {1}\r\nSQLite {2}',
                    'about_hardwf': 'Hardware',
                    'about_hardwv': '**CPU:** {0} ({1} MHz)\r\n**RAM:** {2}\r\n**Platform:** {3}',
                    'about_linksf': 'Links',
                    'about_linksv': '[Invite]({0})',
                    'about_linksv2': '[Website]({0})',
                    'about_linksv3': '[Source code]({0}) (Apache License 2.0 & AGPL 3.0+)',
                    'about_linksv4': '[Support server]({0})',
                    'about_linksv5': '[YouTube channel]({0})',
                    'user_nickf': 'Nickname',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Missing*',
                    'user_regdf': 'Registration date',
                    'user_regdv': '{0}',
                    'user_joinf': 'Server join date',
                    'user_joinv': '{0}',
                    'user_statusf': 'Status',
                    'user_statusv': '<:online:1012294415731146765> Online',
                    'user_statusv2': '<:idle:1012294411020947457> Idle',
                    'user_statusv3': '<:dnd:1012294408412082186> DND',
                    'user_statusv4': '<:offline:1012294452246753300> Offline',
                    'user_rolesf': 'Roles ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Owner',
                    'guild_ownerv': '{0} (`{1}#{2}`)',
                    'guild_crtf': 'Date of creation',
                    'guild_crtv': '{0}',
                    'guild_mlvlf': 'Moderation degree',
                    'guild_mlvlv': 'Without limits',
                    'guild_mlvlv2': 'Only confirmed e-mail',
                    'guild_mlvlv3': 'Registration over 5 minutes',
                    'guild_mlvlv4': 'Presence over 10 minutes',
                    'guild_mlvlv5': 'Only confirmed phone',
                    'guild_blvlf': 'Boost level',
                    'guild_blvlv': 'Level {0}',
                    'guild_statsf': 'Statistics',
                    'guild_statsv': '**{0} members total**\r\n👤 {1} ({2}%)\r\n🤖 {3} ({4}%)\r\n<:online:1012294415731146765> {5} ({6}%)\r\n<:channels:1012296573364998196> {7}',
                    'guild_rulesf': 'Rules',
                    'guild_rulesv': '{0}',
                    'guild_featurf': 'Features',
                    'guild_featurv': 'Automod',
                    'guild_featurv2': 'Community',
                    'guild_featurv3': 'News',
                    'guild_featurv4': 'Text in voice ch.',
                    'guild_featurv5': 'Welcome screen',
                    '8ball_answf': 'Answer',
                    '8ball_answv': ['Yes.', 'No.', 'Maybe.', 'Time will tell.', 'Wait and see.', 'Unlikely.', 'Of course.', 'Yep.', 'Nope.', 'And there is.', 'I have no idea.', 'I don\'t know', 'No idea.', 'Maybe yes...', 'Maybe no...', 'Who knows!', 'I didn\'t understand your question, can you repeat?', 'Try asking a different question. Maybe I don\'t understand something?', 'Probably.', 'Nothing like this.'],
                    'rngen_numbf': 'Number',
                    'rngen_numbv': '{0}',
                    'ping_statisticsf': 'Statistics',
                    'ping_statisticsv': '**Latency:** {0} msec',
                    'ping_statisticsv2': '**Latency:** {0} msec\r\n**Execution time:** {1} msec',
                    'settings_availoptf': 'Available options',
                    'settings_availoptv': '🚩 Язык (Language)\r\n🪄 Prefix',
                }
            elif where == "command_description":
                locale = {
                    'help': 'Shows help information including a list of available commands.',
                    'about': 'Shows a description of the bot, as well as service information.',
                    'user': 'Shows user info.',
                    'avatar': 'Shows the user\'s avatars.',
                    '8ball': 'Generates a random answer for any question. All matches are random!',
                    'rngen': 'Generates a number in a specified range.',
                    'guild': 'Shows guild (server) info',
                    'calc': 'Simplest calculator.',
                    'settings': 'Bot settings.',
                    'settings_lang': 'Changing bot language.',
                    'publish': 'Publishes messages from news channel without extra clicks on the mouse button.',
                    'ping': 'Ping me.',
                    'weather': 'Displays the weather forecast for the next 24 hours. This is done using the [OpenWeatherMap](https://openweathermap.org) service.',
                    'wiki': 'Displays a Wikipedia article in short form.',
                    'codec': 'Decoding and coding of text.'
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'All matches are random!'
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@mention or member ID]```',
                    'avatar': '```{0}avatar [@mention or member ID]```',
                    '8ball': '```{0}8ball [question]```',
                    'rngen': '```{0}rngen [beginning of range]-[end of range]```',
                    'guild': '```{0}guild```',
                    'calc': '```{0}calc [expression]```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L ru_RU```',
                    'settings_prefix': '```{0}settings -P m!```',
                    'ping': '```{0}ping```',
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Show avatar',
                    'rngen_retry': 'Retry',
                }
            elif where == "numb_with_unit":
                locale = {
                    'bytes': '{0} bytes',
                    'bytes2': '{0} / {1} bytes',
                    'kilobytes': '{0} kB',
                    'kilobytes2': '{0} / {1} kB',
                    'megabytes': '{0} MB',
                    'megabytes2': '{0} / {1} MB',
                    'gigabytes': '{0} GB',
                    'gigabytes2': '{0} / {1} GB',
                }
            else:
                locale = {
                }
            if len(locale) == 0: # if string not found (variant #1)
                return "[{0}|{1}] String not found".format(str, where)
            else:
                return locale[str]
    except:
            if language == "ru_RU": # if string not found (variant #2)
                return "[{0}|{1}] Строка не найдена".format(str, where)
            else:
                return "[{0}|{1}] String not found".format(str, where)

def getLanguages():
    languages = {'ru_RU': 'Russian', 'en_US': 'English'}
    return languages
