from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from database import fetch_user, update_user
from datetime import datetime
from aiogram.utils.text_decorations import markdown_decoration

from keyboards import get_miner_stat_keyboard

router = Router()

@router.message(Command('miner'))
async def get_miner(msg: Message):
    '''Fetch information about user's miner'''
    delta, income = await update_miner(msg.from_user.id)
    if delta == -1:
        await msg.answer('*You are not registered\!*')
        return
    mins = int(delta // 60)
    data = await fetch_user(msg.from_user.id)
    miners = data[2]
    text = f'''🪙 *Here are stats of your farm:*

> 🧑‍💼 Owner: _*{markdown_decoration.quote(data[1])}*_
> ⛏️ {miners} miners
> 💵 {income} CLK collectable
> ⌛ {mins} minutes ago you collected CLK'''
    await msg.answer(text, reply_markup=get_miner_stat_keyboard())


@router.callback_query(F.data == 'collect_miners_income')
async def collect_miners_income(callback: CallbackQuery):
    data = await fetch_user(callback.from_user.id)
    if data is None:
        await callback.message.answer('*You are not registered\!*')
        return -1, -1
    _, income = await update_miner(callback.from_user.id)
    await update_user(callback.from_user.id, {'cash': data[3] + income, 'ltm': datetime.isoformat(datetime.now())})
    await callback.message.answer(f'''👍 You successfully collected {income} CLK''')
    await callback.answer()


async def update_miner(telegram_id: int) -> int:
    data = await fetch_user(telegram_id)
    if data is None:
        return -1, -1
    time = datetime.fromisoformat(data[4])
    miners = data[2]
    now = datetime.now()
    delta = (now - time).total_seconds()
    income = int(delta // 60 * miners * 100)
    cash = data[3]
    cash += income
    return delta, income