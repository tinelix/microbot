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
    guilds_query = '''CREATE TABLE IF NOT EXISTS servers (
                id TEXT NOT NULL PRIMARY KEY,
                language TEXT NOT NULL,
                prefix TEXT NOT NULL,
                bot_ch_id INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL);'''
    cursor.execute(guilds_query)
    users_query = '''CREATE TABLE IF NOT EXISTS users (
                id TEXT NOT NULL PRIMARY KEY,
                reputation INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL,
                sended_msg_timestamp DATETIME NOT NULL,
                blocked INTEGER NOT NULL);'''
    cursor.execute(users_query)
    database.commit()

async def add_server_value(database, server, cursor):
    query = """INSERT INTO servers VALUES (?, ?, ?, ?, ?);"""
    values = [(server.id, "en_US", ">", 0, now.strftime('%Y-%m-%d %H:%M:%S'))]
    cursor.executemany(query, values)
    database.commit()

async def add_user_value(database, message, cursor):
    query = """INSERT INTO users VALUES (?, ?, ?, ?, ?);"""
    values = [(message.author.id, 0, now.strftime('%Y-%m-%d %H:%M:%S'), datetime.datetime.fromtimestamp(message.created_at).strftime('%Y-%m-%d %H:%M:%S'), 0)]
    cursor.executemany(query, values)
    database.commit()

async def update_value(ctx, database, cursor, table, key, value, id):
    query = """UPDATE {0} SET {1} = {2} WHERE id = '{3}'""".format(table, key, value, id)
    cursor.execute(query)
    database.commit()

async def if_user_existed(database, cursor, id):
    query = """SELECT EXISTS(SELECT 1 FROM users WHERE id = '{0}' LIMIT 1)""".format(id)
    existed = cursor.execute(query)
    if(existed.fetchone()[0] == 1):
        return True
    else:
        return False

async def if_server_existed(database, cursor, id):
    query = """SELECT EXISTS(SELECT 1 FROM servers WHERE id = '{0}' LIMIT 1)""".format(id)
    existed = cursor.execute(query)
    if(existed.fetchone()[0] == 1):
        return True
    else:
        return False
