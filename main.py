from aiogram import Bot, Dispatcher, executor, types
from classes import *
from lists import *

TOKEN = '5599993276:AAFmRTWMwwqa-MW5gwsxIMf85r0bTD4Kfm4'

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


# frenchpress = 'frenchpress.jpg'


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello')


# пользователю придлагается список упражнеий на группы мышц для ознакомления
@dp.message_handler(commands=['exercises'])
async def command_exercises(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Список упражнений по группам мышц, чтобы наглядно увидеть выполнение упражнения, '
                           'щелкните по названию упражнения:\n\n'
                           '<b>Руки:</b> \n'
                           '/biceps - упражнения на бицепс\n'
                           '/triceps - упражнения на трицепс\n'
                           '/wrists - упражнения для развития запястий\n\n'
                           '<b>Грудь:</b>\n'
                           '/chest - упражнения на грудные мышцы\n\n'
                           '<b>Спина:</b>\n'
                           '/back - упражнения на спину\n\n'
                           '<b>Плечи:</b>\n'
                           '/shoulders - упражнения на плечи\n\n'
                           '<b>Ноги:</b>\n'
                           '/legs - упражнения на ноги\n\n'
                           '<b>Пресс</b>\n'
                           '/press - упражнения на пресс \n\n'
                           '<b>Упражнения с собственным весом:</b>\n'
                           '/ownweight - упражнения для тренировки с собственным весом\n'
                           '<b>Кардио и жиросжигание</b>\n\n'
                           '/cardio - кардио тренировка')


# упражнения на бицепс
@dp.message_handler(commands=['biceps'])
async def command_biceps(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Упражнения для развития бицепса. Возможно выполнение 3-4 упражнений с большими весами по'
                           '4-5 подходов на 10-12 повторений каждый, либо выполнение 2-3 упражнений подряд'
                           'по 4-5 подходов на 6-8 повторений каждый с весами поменьше')
    await ExercisesGenerator.list_exercires(biceps, message.from_user.id)


# упражнения на трицепс
@dp.message_handler(commands=['triceps'])
async def command_triceps(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития трицепса. Оптимально выполнять 3-4 упражнения'
                                                 ' по 4-5 подходов на 10-12 повторений в каждом подходе.'
                                                 'Возможно комбинировать 2 упражнения выполняя подряд')
    await ExercisesGenerator.list_exercires(triceps, message.from_user.id)


# упражнения на запястья
@dp.message_handler(commands=['wrists'])
async def command_wrists(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития запястий: \n')
    await ExercisesGenerator.list_exercires(wrists, message.from_user.id)


# упражнения на грудь
@dp.message_handler(commands=['chest'])
async def command_chest(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития грудных мышц: \n')
    await ExercisesGenerator.list_exercires(chest, message.from_user.id)


# упражнения на спину
@dp.message_handler(commands=['back'])
async def command_back(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития мышц спины: \n')
    await ExercisesGenerator.list_exercires(back, message.from_user.id)


# упражнения на плечи
@dp.message_handler(commands=['shoulders'])
async def command_shoulders(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития плечевых мышц: \n')
    await ExercisesGenerator.list_exercires(shoulders, message.from_user.id)


# упражнения на ноги
@dp.message_handler(commands=['legs'])
async def command_legs(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для развития мышц ног: \n')
    await ExercisesGenerator.list_exercires(legs, message.from_user.id)


# упражнения для прокачки пресса
@dp.message_handler(commands=['press'])
async def command_press(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для прокачки пресса: \n')
    await ExercisesGenerator.list_exercires(press, message.from_user.id)


# упражнения для прокачки тела с собственным весом
@dp.message_handler(commands=['ownweight'])
async def command_press(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для прокачки тела с собственным весом: \n')
    await ExercisesGenerator.list_exercires(ownweight, message.from_user.id)


# упражнения для кардио тренировки
@dp.message_handler(commands=['cardio'])
async def command_press(message: types.Message):
    await bot.send_message(message.from_user.id, 'Упражнения для кардио тренировки: \n')
    await ExercisesGenerator.list_exercires(cardio, message.from_user.id)


# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
