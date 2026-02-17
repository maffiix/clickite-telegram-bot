import aiosqlite
import datetime


async def fetch_user(telegram_id: int):
    '''Function for fetching one user from database bot.db'''
    _, cursor = await connect()
    await cursor.execute('SELECT * FROM users WHERE id=?', (telegram_id,))
    return await cursor.fetchone()


async def insert_user(telegram_id: int, nickname: str):
    '''Insert user to the database'''
    connection, cursor = await connect()
    now = datetime.datetime.isoformat(datetime.datetime.now())
    await cursor.execute('INSERT INTO users (id, name, ltm) VALUES (?, ?, ?)', (telegram_id, nickname, now))
    await connection.commit()


async def update_user(telegram_id: int, values: dict):
    '''Update user data'''
    connecion, cursor = await connect()
    request = []
    for key in values.keys():
        request.append(f'{key} = ?')
    request = ', '.join(request)
    await cursor.execute(f'UPDATE users SET {request} WHERE id=?', tuple(list(values.values()) + [telegram_id]))
    await connecion.commit()


async def connect():
    '''Connect to the database'''
    connection = await aiosqlite.connect('bot.db')
    cursor = await connection.cursor()
    return connection, cursor