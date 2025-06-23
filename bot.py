from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

def calculate_matrix(date_str):
    nums = [int(char) for char in date_str if char.isdigit()]
    first_sum = sum(nums)
    second_sum = sum(int(c) for c in str(first_sum))
    third_sum = first_sum - 2 * int(date_str[0])
    fourth_sum = sum(int(c) for c in str(third_sum))

    all_numbers = nums + [int(i) for i in str(first_sum) + str(second_sum) + str(third_sum) + str(fourth_sum)]
    matrix = {str(i): all_numbers.count(i) for i in range(1, 10)}

    result = "\n".join(f"{k}: {v}" for k, v in matrix.items())
    return result

@dp.message(Command(commands=["start"]))
async def start_command(message: types.Message):
    await message.answer("Привет! Введи дату рождения в формате ДД.ММ.ГГГГ:")

@dp.message()
async def handle_message(message: types.Message):
    date_str = message.text.strip()
    try:
        result = calculate_matrix(date_str)
        await message.answer(f"Матрица судьбы для {date_str}:\n\n{result}")
    except Exception:
        await message.answer("Ошибка! Введи дату в формате ДД.ММ.ГГГГ")

if __name__ == "__main__":
    dp.start_polling(bot)
