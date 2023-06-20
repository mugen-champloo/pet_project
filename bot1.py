import logging
import asyncio
import data
from data import last_data, delete_last_data
import dataparsing
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.filters import Text
from export_to_exel import export
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5891958326:AAEb-PZXDJNPNL2B274C0JfV2827TPAezW4')

dp = Dispatcher()



@dp.message(Command('start', 'help'))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Помощь")],
        [types.KeyboardButton(text="Вывести отчет")],
        [types.KeyboardButton(text='Удалить последнюю')],
        [types.KeyboardButton(text='Удалить определнную')], 
        [types.KeyboardButton(text='Добавить в определенную дату')],
        [types.KeyboardButton(text='Всего потрачено')]

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Наберите ваше сообщение'
    )
    await message.answer(f'Бот для ввода и вывода данных о расходах \n\n'
                         f'Формат добавления данных: \n'
                         f'Распредвалы.. 4444.. 4шт.. 80000.. 90000\n\n'
                         f'Тоесть:\n'
                         f'(Наименование).. (Техниика, не обязат.).. (Количество, не обязат.).. (Цена).. (Приход, если нету то 0)\n\n'
                         f'.. Две точки для разделения между данными', reply_markup=keyboard)

@dp.message(Text("Вывести отчет"))
async def send_report(message: types.Message):
    a = export()
    # a = data.report
    # for i in a:
    #     await message.answer(i)
    # with open(a, "rb") as file:
    #     input_file = InputFile(file) 5891958326
    document = FSInputFile(a)
    await bot.send_document('452367296', document)

@dp.message(Text("Помощь"))
async def enter_data(message: types.Message):
    await message.reply(f'Формат добавления данных: \n'
                         f'Распредвалы.. 4444.. 4шт.. 80000.. 90000\n\n'
                         f'Тоесть:\n'
                         f'(Наименование).. (Техниика, не обязат.).. (Количество, не обязат.).. (Цена).. (Приход, если нету то 0)\n\n'
                         f'.. Две точки для разделения между данными')

@dp.message(Text("Всего потрачено"))
async def enter_data(message: types.Message):
    await message.reply(data.sum_for_print())

@dp.message(Text("Удалить последнюю"))
async def delete_last(message: types.Message):
    a = last_data()
    delete_last_data()
    await message.answer(f'Удалил последнюю запись: {a}')

@dp.message(Text('Удалить определнную'))
async def delete_specific(message: types.Message):
    await message.answer(f'Формат удаления данных: \n\n'
                         f'Удали [Id записаи]\n'
                         f'Удали 19')

@dp.message(Text('Добавить в определенную дату'))
async def delete_specific(message: types.Message):
    await message.answer(f'Формат добавления данных в определенную дату: \n\n'
                         f'01.01.2021.. Единицы.. Гурам.. .. 200..\n')

@dp.message()
async def writedata(message: types.Message):
    a = dataparsing.parser(message.text)
    await message.answer(a)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
