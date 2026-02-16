from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def greet(msg: Message):
    '''Handle /start command'''
    text = f'''*Welcome to Clickite Miner\!* 🎮

Soon here you will be able to see channel \+ chat links'''
    await msg.answer(text)


@router.message(Command('help'))
async def help(msg: Message):
    '''Handle /help command'''
    help_msg = f'''*Welcome to Clickite's Help\!*

📜 _Here are some of the available commands:_**
\- `/start` \- shows greeting message
\- `/help` \- shows this message'''
    await msg.answer(help_msg)