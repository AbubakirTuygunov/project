
from aiogram import Bot, Dispatcher, types, filters, F
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token="7332168348:AAGXYaxedlMXuxE4qnRvYCbeGiHCzyITnuY")
dp = Dispatcher(bot=bot)

language = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Uzbek tili 🇺🇿"), KeyboardButton(text="Русский язык 🇷🇺")],
], resize_keyboard=True)

menu_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Kurslar"), KeyboardButton(text="Savat"), KeyboardButton(text="Biz haqimizda")],
    [KeyboardButton(text="Qo'llab-quvvatlash"), KeyboardButton(text="Tilni o'zgartirish")],
    [KeyboardButton(text="Kontakt ulashish", request_contact=True)]
], resize_keyboard=True)

menu_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Курсы"), KeyboardButton(text="Корзинк"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="Поддержка"), KeyboardButton(text="Язык")],
    [KeyboardButton(text="Поделиться контактом", request_contact=True)]
], resize_keyboard=True)

courses_keyboard_uz = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Inter Nation School"), KeyboardButton(text="Mars It School")],
    [KeyboardButton(text="Yuksalish LEADERS ACADEMY"), KeyboardButton(text="My-School")],
    [KeyboardButton(text="CodeCraft Academy"), KeyboardButton(text="Tech Innovators")],
    [KeyboardButton(text="Orqaga↩")]
], resize_keyboard=True)

courses_keyboard_ru = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Inter_Nation_School"), KeyboardButton(text="Mars_It_School")],
    [KeyboardButton(text="Yuksalish_LEADERS_ACADEMY"), KeyboardButton(text="My_School")],
    [KeyboardButton(text="CodeCraft_Academy"), KeyboardButton(text="Tech_Innovators")],
    [KeyboardButton(text="Назад")]
], resize_keyboard=True)


course_keyboard_uz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Sotib olish ", callback_data="Sotib olish ")],
    [InlineKeyboardButton(text="Bekor qilish ", callback_data="Bekor qilish ")]
])

course_keyboard_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Купить ", callback_data="Купить ")],
    [InlineKeyboardButton(text="Отменить ", callback_data="Отменить ")]
])


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer("Tilini tanlang :\nВыберите язык :", reply_markup=language)


@dp.message(F.text == "Uzbek tili 🇺🇿")
async def uz_language(message: types.Message):
    await message.answer("Siz Uzbek tilini tanladingiz", reply_markup=menu_uz)


@dp.message(F.text == "Русский язык 🇷🇺")
async def ru_language(message: types.Message):
    await message.answer("Вы выбрали русский язык 🇷🇺", reply_markup=menu_ru)


@dp.message(F.text == "Kurslar")
async def course_menu_uz(message: types.Message):
    await message.answer("Kursni tanlang:", reply_markup=courses_keyboard_uz)


@dp.message(F.text == "Курсы")
async def course_menu_ru(message: types.Message):
    await message.answer("Выберите курс:", reply_markup=courses_keyboard_ru)


@dp.message(F.text == "Savat")
async def cart_uz(message: types.Message):
    await message.answer("Savat bo'sh:")


@dp.message(F.text == "Корзинка")
async def cart_ru(message: types.Message):
    await message.answer("Корзинка:")


@dp.message(F.text == "Biz haqimizda")
async def about_us_uz(message: types.Message):
    photo = "https://png.klev.club/uploads/posts/2024-04/png-klev-club-qmhl-p-podderzhka-png-30.png"
    await message.answer_photo(photo=photo, caption="Biz haqimizda:\n Biz sizga kurs talashka yordam beramiz \n Koshimcha malumot uchun: +998(91)-451-04-50", reply_markup=menu_uz)


@dp.message(F.text == "О нас")
async def about_us_ru(message: types.Message):
    photo = "https://png.klev.club/uploads/posts/2024-04/png-klev-club-qmhl-p-podderzhka-png-30.png"
    await message.answer_photo(photo=photo, caption="О нас:\nМы для вас помогаем найти курсы\n Для подершки: +998(91)-451-04-50", reply_markup=menu_ru)





@dp.message(F.text == "Qo'llab-quvvatlash")
async def support_uz(message: types.Message):
    await message.answer("Qo'llab-quvvatlash: ChatGPT bilan suhbat")


@dp.message(F.text == "Поддержка")
async def support_ru(message: types.Message):
    await message.answer("Поддержка: чат с ChatGPT")


@dp.message(F.text == "Tilni o'zgartirish")
async def change_language_uz(message: types.Message):
    await message.answer("Tilni o'zgartirish", reply_markup=language)


@dp.message(F.text == "Язык")
async def change_language_ru(message: types.Message):
    await message.answer("Поменять язык", reply_markup=language)


@dp.message(F.text == "Orqaga")
async def back_uz(message: types.Message):
    await message.answer("Bosh menyuga qaytish", reply_markup=menu_uz)


@dp.message(F.text == "Назад")
async def back_ru(message: types.Message):
    await message.answer("Возвращение в главное меню", reply_markup=menu_ru)


@dp.message(F.text == "Inter_Nation_School")
async def inter_nation_school_ru(message: types.Message):
    photo = "https://inter-nation.uz/_next/image?url=%2Fbranches%2FOybek.webp&w=1080&q=75"
    await message.answer_photo(photo=photo, caption="Inter Nation School \n "
        "INTER NATION SCHOOL INGLIZ TILI O'QUV MARKAZI Ta'lim Oksford universiteti (Oxford University Press) tomonidan ishlab chiqilgan maxsus dastur "
        "bo'yicha olib boriladi, bu eng yaxshilaridan biri hisoblanadi!\n888.000 som", reply_markup=course_keyboard_uz)


@dp.message(F.text == "Inter Nation School")
async def inter_nation_school_uz(message: types.Message):
    photo = "https://inter-nation.uz/_next/image?url=%2Fbranches%2FOybek.webp&w=1080&q=75"
    await message.answer_photo(photo=photo, caption="Inter Nation School\n "
      "УЧЕБНЫЙ ЦЕНТР английского языка INTER NATION SCHOOL Обучение ведётся по специальной программе, разработанной "
      "Оксфордским университетом (Oxford University Press), являющейся одной из лучших!\n888.000 сум💲", reply_markup=course_keyboard_ru)


@dp.message(F.text == "Mars It School")
async def mars_it_school_uz(message: types.Message):
    photo = "https://static.tildacdn.com/tild6334-3862-4566-b832-363266346634/156.png"
    await message.answer_photo(photo=photo, caption="Mars It School \n «Mars IT»da o'qish kimlar uchun mos keladi?Darslar "
        "8 yoshdan 18 yoshgacha barcha bolalar uchun, ayniqsa kompyuter "
        "o'yinlaridan chalg'imaydigan va dasturlash olamiga qiziqishi katta bo'lganlar uchun.\n1.090.000 som💲", reply_markup=course_keyboard_uz)


@dp.message(F.text == "Mars_It_School")
async def mars_it_school_ru(message: types.Message):
    photo = "https://static.tildacdn.com/tild6334-3862-4566-b832-363266346634/156.png"
    await message.answer_photo(photo=photo, caption="Mars It School \n Кому подходит обучение в «Mars IT»?Занятия подойдут всем детям в "
     "возрасте 8-18 лет, особенно тем, которых не оторвать от компьютерных игр и у них уже есть большой интерес к миру программирования\n1.090.000 сум💲", reply_markup=course_keyboard_ru)


@dp.message(F.text == "Yuksalish LEADERS ACADEMY")
async def yuksalish_uz(message: types.Message):
    photo = "https://framerusercontent.com/images/zn5Rl3JR4YQjLBMggIVMXrTOA7g.png"
    await message.answer_photo(photo=photo, caption="Yuksalish LEADERS ACADEMY®\n \n1.100.000 som", reply_markup=course_keyboard_uz)


@dp.message(F.text == "Yuksalish_LEADERS_ACADEMY")
async def yuksalish_ru(message: types.Message):
    photo = "https://framerusercontent.com/images/zn5Rl3JR4YQjLBMggIVMXrTOA7g.png"
    await message.answer_photo(photo=photo, caption="Yuksalish LEADERS ACADEMY®\n1.100.000 сум", reply_markup=course_keyboard_ru)


@dp.message(F.text == "My-School")
async def my_school_uz(message: types.Message):
    photo = "https://hh.uz/employer-logo/3778216.png"
    await message.answer_photo(photo=photo, caption="My School \n Oksford universiteti (Oxford University Press) tomonidan ishlab chiqilgan maxsus dastur "
        "bo'yicha olib boriladi, bu eng yaxshilaridan biri hisoblanadi!\n750.000 som", reply_markup=course_keyboard_uz)





@dp.message(F.text == "My_School")
async def my_school_ru(message: types.Message):
    photo = "https://hh.uz/employer-logo/3778216.png"
    await message.answer_photo(photo=photo, caption="My School \n Обучение ведётся по специальной программе, разработанной "
      "Оксфордским университетом (Oxford University Press), являющейся одной из лучших!\n750.000 сум💲", reply_markup=course_keyboard_ru)


@dp.message(F.text == "CodeCraft Academy🖥")
async def codecraft_academy_uz(message: types.Message):
    photo = "https://codecraft.uz/assets/bannerImg-72809434.png"
    await message.answer_photo(photo=photo, caption="CodeCraft Academy \nDarslar 8 yoshdan 18 yoshgacha barcha bolalar uchun, ayniqsa kompyuter "
        "o'yinlaridan chalg'imaydigan va dasturlash olamiga qiziqishi katta bo'lganlar uchun. \n950.000 som💲", reply_markup=course_keyboard_uz)


@dp.message(F.text == "CodeCraft_Academy🖥")
async def codecraft_academy_ru(message: types.Message):
    photo = "https://codecraft.uz/assets/bannerImg-72809434.png"
    await message.answer_photo(photo=photo, caption="CodeCraft Academy️\nЗанятия подойдут всем детям в "
      "возрасте 8-18 лет, особенно тем, которых не оторвать от компьютерных "
      "игр и у них уже есть большой интерес к миру программирования \n950.000 суm", reply_markup=course_keyboard_ru)


@dp.message(F.text == "Tech Innovators")
async def tech_innovators_uz(message: types.Message):
    photo = "https://img.freepik.com/premium-vector/innovation-technology-logo_27153-26.jpg"
    await message.answer_photo(photo=photo, caption="Tech Innovators \nKimgadur investitiyaga kizikayotkan bo'lsangiz"
    "unda bizni jamomizga koshiling biz o'z tajribadan kelib chikan holda barcha kerakli bilimlani beramiz \n1.200.000 som", reply_markup=course_keyboard_uz)


@dp.message(F.text == "Tech_Innovators")
async def tech_innovators_ru(message: types.Message):
    photo = "https://img.freepik.com/premium-vector/innovation-technology-logo_27153-26.jpg"
    await message.answer_photo(photo=photo, caption="Tech Innovators \nЕсли вы интересуетес к инвеститиях то мы вам паможим"
    " пресодинятес к нашим команду мы будем рады всеми знаниями будете обучены  \n1.200.000 сум", reply_markup=course_keyboard_ru)


@dp.message(F.data == "Sotib olish ")
async def buy_course(callback_query: types.CallbackQuery):
    await callback_query.answer("Siz kursni sotib oldingiz!\nВы купили курс!", show_alert=True)


@dp.message(F.data == "Bekor qilishv")
async def cancel_course(callback_query: types.CallbackQuery):
    await callback_query.answer("Siz kursni bekor qildingiz.\nВы отменили курс.", show_alert=True)

async def main():

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

