from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_miner_stat_keyboard():
    '''Return keyboard for mining stats'''
    builder = InlineKeyboardBuilder()

    builder.button(text='💰 Collect CLK!', callback_data='collect_miners_income')
    builder.adjust(1, 1)

    return builder.as_markup()