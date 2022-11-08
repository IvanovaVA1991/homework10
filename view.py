from aiogram import types

from bot import bot
import random
import model

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           'Это игра в конфетки\n'
                           'Чтобы узнать правила, набери команду /rules\n'
                           'Чтобы начать новую игру, введи команду /game\n'
                           'Чтобы закончить такущую игру, введи команду /finish')

async def rules(message: types.Message):
    await bot.send_message(message.from_user.id, 'На столе лежит 150 конфет. Кто ходит первым, определяется рандомно.\n'
                        'За один ход можно забрать от 1 до 28 конфет.\n'
                        'Все конфеты оппонента достаются сделавшему последний ход.')

async def finish(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'Игра окончена. Чтобы начать новую игру, введи команду /game\n'
                        'Если хочешь еще раз прочитать правила - команда /rules')

async def game(message: types.Message):
    model.firstPlayer = random.randint(1, 2)    #1-user, 2 - bot
    if model.firstPlayer == 1:
        await message.answer('Ходи первым! Напиши количество конфет')
    else:
        model.count = model.total_count%(model.max_turn+1)
        model.total_count -= model.count
        await message.answer(f'Я хожу первым и беру {model.count} конфет. Осталось {model.total_count} конфет.\n'
                                'Твой ход!')