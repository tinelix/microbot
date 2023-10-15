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

import datetime

now = datetime.datetime.now()

async def create_tables(database, cursor):
    guilds_query = '''CREATE TABLE IF NOT EXISTS guilds (
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(80) NOT NULL,
                language VARCHAR(20) NOT NULL,
                prefix VARCHAR(8) NOT NULL,
                bot_ch_id INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL);'''
    cursor.execute(guilds_query)
    users_query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY,
                global_name VARCHAR(50) NOT NULL,
                reputation INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL,
                sended_msg_timestamp DATETIME NOT NULL,
                timezone VARCHAR(8) NOT NULL,
                blocked INTEGER NOT NULL);'''
    cursor.execute(users_query)
    timers_query = '''CREATE TABLE IF NOT EXISTS timers (
                name VARCHAR(100) NOT NULL,
                author_id INTEGER NOT NULL,
                icon VARCHAR(20) NOT NULL,
                timer_action_date DATETIME NOT NULL,
                timer_action VARCHAR(20) NOT NULL,
                over INTEGER NOT NULL);'''
    cursor.execute(timers_query)
    database.commit()

async def add_guild_value(config, database, guild, cursor):
    query = """INSERT INTO guilds VALUES (?, ?, ?, ?, ?, ?);"""
    values = [(guild.id, guild.name, "en_US", config['prefix'], 0, now.strftime('%Y-%m-%d %H:%M:%S'))]
    cursor.executemany(query, values)
    database.commit()

async def add_user_value(database, message, cursor):
    query = """INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?);"""
    values = [(message.author.id, message.author.global_name, 0, now.strftime('%Y-%m-%d %H:%M:%S'), message.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'Europe/Moscow', 0)]
    cursor.executemany(query, values)
    database.commit()

async def add_timer_value(database, id, icon, name, time, action, cursor):
    query = """INSERT INTO timers VALUES (?, ?, ?, ?, ?, ?);"""
    values = [(name, id, icon, time, action, 0)]
    cursor.executemany(query, values)
    database.commit()

async def update_value(ctx, database, cursor, table, key, value, id):
    query = """UPDATE {0} SET {1} = {2} WHERE id = {3}""".format(table, key, value, id)
    cursor.execute(query)
    database.commit()

async def update_timer_value(ctx, database, cursor, key, value, name):
    query = """UPDATE timers SET {1} = {2} WHERE name = {3}""".format(key, value, name)
    cursor.execute(query)
    database.commit()

async def if_user_existed(database, cursor, id):
    query = """SELECT EXISTS(SELECT 1 FROM users WHERE id = {0} LIMIT 1)""".format(id)
    existed = cursor.execute(query)
    if(existed.fetchone()[0] == 1):
        return True
    else:
        return False

async def if_guild_existed(database, cursor, id):
    query = """SELECT EXISTS(SELECT 1 FROM guilds WHERE id = {0} LIMIT 1)""".format(id)
    existed = cursor.execute(query)
    if(existed.fetchone()[0] == 1):
        return True
    else:
        return False

async def get_timers_by_user(database, cursor, id):
    cursor.execute("SELECT * FROM timers WHERE author_id='{0}';".format(id))
    timers_data = cursor.fetchall()
    return timers_data

async def delete_timer(database, cursor, name, id):
    cursor.execute("""DELETE FROM timers WHERE name = '{0}' AND author_id = {1};""".format(name, id))
    database.commit()
    return "OK!"
