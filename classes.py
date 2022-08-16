#метод класса отправляет в чат сообщения с выборкой всех упражнений по выбранной группе мышц
class ExercisesGenerator:
    @classmethod
    async def list_exercires(cls, exerciseslist, message=None):
        for i in exerciseslist:
            with open(i, 'rb') as photo:
                from main import bot
                await bot.send_message(message, exerciseslist[i])
                await bot.send_photo(message, photo=photo, disable_notification=True)
                photo.close()
