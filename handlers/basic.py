from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database import fetch_user, insert_user
from aiogram.utils.text_decorations import markdown_decoration

router = Router()


@router.message(Command('start'))
async def greet(msg: Message):
    '''Handle /start command'''
    text = f'''*Welcome to Clickite Miner\!* 🎮

Soon here you will be able to see channel \+ chat links'''
    response = await fetch_user(msg.from_user.id)
    print(response)
    if response is None:
        text += '\n\n'
        text += f'''You are not registered in this bot\nTo use its features, please type /register'''
    await msg.answer(text)


@router.message(Command('help'))
async def help(msg: Message):
    '''Handle /help command'''
    help_msg = f'''*Welcome to Clickite's Help\!*

📜 _Here are some of the available commands:_**
\- `/start` \- shows greeting message
\- `/help` \- shows this message'''
    await msg.answer(help_msg)


@router.message(Command('register'))
async def register(msg: Message):
    '''Register new user to the bot'''
    name = msg.from_user.first_name
    if not name:
        name = 'Player'
    try:
        await insert_user(msg.from_user.id, name)
        response = f'''🚀 *You successfully registered\!*

📋 _Here is your information:_
  🏷️ Name: {markdown_decoration.quote(name)}
  🆔 ID: `{msg.from_user.id}`
  💸 CLK: 0'''
    except Exception as e:
        response = f'''*You already registered\!*'''
    await msg.answer(response)


@router.message(Command('profile'))
@router.message(Command('me'))
async def profile(msg: Message):
    response = await fetch_user(msg.from_user.id)
    if response is not None:
        name = response[1]
        text = f'''👤 *Here is your profile\.*

🏷️ _Nickname:_ _*{name}*_
🆔 _ID:_ `{msg.from_user.id}`
💸 _CLK:_ {response[3]}'''
    else:
        text = f'''Sorry, cant find you 😩
_Type `/register` to start\.\.\._'''
    
    await msg.answer(text)
