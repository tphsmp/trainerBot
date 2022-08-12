from aiogram import Bot, Dispatcher, executor, types

# from aiogram.types import InputFile

TOKEN = ''

bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


# barbel_curls = InputFile('barbel_curls.jpg', 'rb')

# frenchpress = InputFile('frenchpress.jpg')
# dumpbell_frenchpress = InputFile('dumpbell_frenchpress.jpg')

# dumpbellfingerpull = InputFile('dumpbellfingerpull.jpg')
# burpbellpull = InputFile('burpbellpull.jpg')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello')


@dp.message_handler(commands=['exercises'])
async def command_exercises(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Список упражнений по группам мышц, чтобы наглядно увидеть выполнение упражнения, '
                           'щелкните по названию упражнения:\n\n'
                           '<b>Руки:</b> \n'
                           '/bicepcurls - упражнения на бицепс\n'
                           '/tricepcurls - упражнения на трицепс\n'
                           '/wrists - упражнения для развития запястий\n\n'
                           '<b>Грудь:</b>\n'
                           '/chest - упражнения на грудные мышцы\n\n'
                           '<b>Спина:</b>\n'
                           '/back - упражнения на спину\n\n'
                           '<b>Плечи:</b>\n'
                           '/shoulders - упражнения на плечи\n\n'
                           '<b>Ноги:</b>\n'
                           '/legs - упражнения на ноги\n\n'
                           '<b>Упражнения с собственным весом:</b>\n'
                           '/ownweight - упражнения для тренировки с собственным весом\n')


@dp.message_handler(commands=['bicepcurls'])
async def command_bicepcurls(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Есть несколько вариантнов упражнений на разитие бицепса. Возможно как очередное '
                           'выполнение так и выполнение сетами по 2-3 упражнения. Подробнее в разделе программы '
                           'тренировок /trains: \n'
                           'Подъем штанги на бицепс:')
    with open('barbellcurls.jpg', 'rb') as barbel_curls:
        await bot.send_photo(message.from_user.id, photo=barbel_curls, disable_notification=True)
        barbel_curls.close()
    await bot.send_message(message.from_user.id, 'Подъем штанги на бицепс с Z-грифом:')
    with open('zcurls.jpg', 'rb') as zcurls:
        await bot.send_photo(message.from_user.id, photo=zcurls, disable_notification=True)
        zcurls.close()
    await bot.send_message(message.from_user.id, 'Сгибания на бицепс с гантелями:')
    with open('dumpbellscurls.jpg', 'rb') as dumpbellscurls:
        await bot.send_photo(message.from_user.id, photo=dumpbellscurls, disable_notification=True)
        dumpbellscurls.close()
    await bot.send_message(message.from_user.id, 'Молот с гантелями:')
    with open('hummercurls.jpg', 'rb') as hummercurls:
        await bot.send_photo(message.from_user.id, photo=hummercurls, disable_notification=True)
        hummercurls.close()
    await bot.send_message(message.from_user.id, 'Изолированные сгибания:')
    with open('isolatedcurls.jpg', 'rb') as isolatedcurls:
        await bot.send_photo(message.from_user.id, photo=isolatedcurls, disable_notification=True)
        isolatedcurls.close()
    await bot.send_message(message.from_user.id, 'Подтягивания обратным хватом:')
    with open('reversepullups.jpg', 'rb') as reversepullups:
        await bot.send_photo(message.from_user.id, photo=reversepullups, disable_notification=True)
        reversepullups.close()


@dp.message_handler(commands=['tricepcurls'])
async def command_tricepcurls(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Есть несколько вариантнов упражнений на разитие трицепса. '
                           'Возможно как очередное выполнение так и выполнение сетами по 2-3 упражнения.'
                           ' Подробнее в разделе программы тренировок /trains: \n'
                           'Французский жим с штангой:')
    with open('frenchpress.jpg', 'rb') as frenchpress:
        await bot.send_photo(message.from_user.id, photo=frenchpress, disable_notification=True)
        frenchpress.close()
    await bot.send_message(message.from_user.id, 'Французский жим с гантелями:')
    with open('dumpbell_frenchpress.jpg', 'rb') as dumpbell_frenchpress:
        # await bot.send_photo(message.from_user.id, photo=InputFile('dumpbell_frenchpress.jpg'))
        await bot.send_photo(message.from_user.id, photo=dumpbell_frenchpress, disable_notification=True)
        dumpbell_frenchpress.close()


@dp.message_handler(commands=['wrists'])
async def command_tricepcurls(message: types.Message):
    await bot.send_message(message.from_user.id, 'Есть несколько вариантнов упражнений на разитие запястий. \n'
                                                 'Тяга гантели пальцами:')
    with open('dumpbellfingerpull.jpg', 'rb') as dumpbellfingerpull:
        await bot.send_photo(message.from_user.id, photo=dumpbellfingerpull, disable_notification=True)
        dumpbellfingerpull.close()
        # await bot.send_photo(message.from_user.id, photo=InputFile('dumpbellfingerpull.jpg'))
    await bot.send_message(message.from_user.id, 'Подъем грифа обратным хватом:')
    with open('burpbellpull.jpg', 'rb') as burpbellpull:
        await bot.send_photo(message.from_user.id, photo=burpbellpull, disable_notification=True)
        burpbellpull.close()
        # await bot.send_photo(message.from_user.id, photo=InputFile('burpbellpull.jpg'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
