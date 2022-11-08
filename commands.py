from aiogram import types
import view
from bot import bot
import model
import random


async def start(message: types.Message):
    await view.greetings(message)


async def rules(message: types.Message):
    await view.rules(message)

async def finish(message: types.Message):
    await view.finish(message)
    model.total_count = 150

async def game(message: types.Message):
    await view.game(message)


async def getNumber(message: types.Message):
    model.count = message.text
    if model.count.isdigit():
        model.count = int(model.count)
        if 0 < model.count < model.max_turn + 1:
            model.total_count -= model.count
            if model.total_count == 150 and model.firstPlayer == 2:
                await message.answer('Для начала новой игры введи команду /game')
            else:
                if model.max_turn*2+1 >= model.total_count > model.max_turn + 1:    # m*2+1 >= n > m + 1   n - total, m - max_turn
                    await message.answer(f'Осталось {model.total_count} конфет')
                    model.count = model.total_count - model.max_turn - 1
                    model.total_count -=  model.count
                    await message.answer(f'Я беру {model.count} конфет. Осталось {model.total_count}')
                elif model.total_count == 0:
                    await message.answer('Поздравляю, ты победил!')
                    await message.answer('Для новой игры введи команду /game.\n'
                                        'Если хочешь еще раз прочитать правила - команда /rules')
                    model.total_count = 150
                elif model.total_count <= model.max_turn:
                    if model.count > model.total_count + model.count:
                        model.total_count += model.count
                        await message.answer(f'Осталось только {model.total_count} конфет, больше взять нельзя!\n'
                                                'Ходи еще раз')
                    else:
                        await message.answer(f'Я беру {model.total_count} конфет и я победил! Бе-бе-бе!')
                        await message.answer('Для новой игры введи команду /game.\n'
                                        'Если хочешь еще раз прочитать правила - команда /rules')
                        model.total_count = 150
                else:
                    await message.answer(f'Осталось {model.total_count} конфет')
                    if model.firstPlayer == 1:
                        model.count = random.randint(1, 28)
                    else:
                        model.count = model.max_turn+1 - model.count
                    model.total_count -=  model.count
                    await message.answer(f'Я беру {model.count} конфет. Осталось {model.total_count}')
        else:
            await message.answer('Ах, ты грязный читер!')
    else:
       await message.answer('Нет такой команды!\n'
                            'Чтобы узнать правила, набери команду /rules\n'
                           'Чтобы начать новую игру, введи команду /game\n') 

        