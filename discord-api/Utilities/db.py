import datetime

now = datetime.datetime.now()

async def create_tables(database, cursor):
    guilds_query = '''CREATE TABLE IF NOT EXISTS guilds (
                id INTEGER NOT NULL PRIMARY KEY,
                language TEXT NOT NULL,
                prefix TEXT NOT NULL,
                bot_ch_id INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL);'''
    cursor.execute(guilds_query)
    users_query = '''CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL PRIMARY KEY,
                reputation INTEGER NOT NULL,
                reg_timestamp DATETIME NOT NULL,
                sended_msg_timestamp DATETIME NOT NULL,
                blocked INTEGER NOT NULL);'''
    cursor.execute(users_query)
    database.commit()

async def add_guild_value(database, guild, cursor):
    query = """INSERT INTO guilds VALUES (?, ?, ?, ?, ?);"""
    values = [(guild.id, "en_US", ">", 0, now.strftime('%Y-%m-%d %H:%M:%S'))]
    cursor.executemany(query, values)
    database.commit()

async def add_user_value(database, message, cursor):
    query = """INSERT INTO users VALUES (?, ?, ?, ?, ?);"""
    values = [(message.author.id, 0, now.strftime('%Y-%m-%d %H:%M:%S'), message.created_at.strftime('%Y-%m-%d %H:%M:%S'), 0)]
    cursor.executemany(query, values)
    database.commit()

async def update_value(ctx, database, cursor, table, key, value, id):
    query = """UPDATE {0} SET {1} = {2} WHERE id = {3}""".format(table, key, value, id)
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
