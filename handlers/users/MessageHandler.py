import asyncio

from aiogram import types
from aiogram.types import reply_keyboard

from loader import dp

from aiogram.dispatcher import filters

from utils.FontsChanger import font_changer, page_generator
from keyboards.inline.InlineKeyboards import generate_buttons
from keyboards.default.main_menu import menu_button
from utils.FontsChanger import fonts_number
from data.Users import specific_font, all_fonts
from utils.db_api.bot_users import create_bot_user

@dp.message_handler(text="📋 Fonts list 📝")
async def menu_handler1(message: types.Message):
    txt = page_generator(1, 10)

    buttons = await generate_buttons(1, 10)
    await message.answer(text=txt, reply_markup=buttons)

@dp.message_handler(text="☑️ Apply all fonts ✅")
async def menu_handler2(message: types.Message):
    all_fonts[message.from_user.id] = True
    
    txt = "<b>Send me some text 🖋</b>"

    await message.answer(text=txt)

@dp.message_handler(text="🤖 About Inline Mode 📃")
async def aboutInlineMode(message: types.Message):
    try:
        await dp.bot.forward_message(
            chat_id=message.from_user.id,
            from_chat_id=-1001702586300,
            message_id=9
        )
    except:
        print("Error while forwarding the Inline Mode video!")

# Echo bot
@dp.message_handler()
async def bot_echo(message: types.Message):

    # Save the user in the database
    create_bot_user(message.from_user)

    user_id = message.from_user.id

    temp1 = all_fonts.get(user_id)
    temp2 = specific_font.get(user_id)

    # Message for admin
    admin_message = f"#U{message.from_user.id}\n\n"
    admin_message += f"<b>Name</b>:   {message.from_user.full_name}\n"
    admin_message += f"<b>ID:</b>    {message.from_user.id}\n"
    admin_message += f"<b>Username:</b>   @{message.from_user.username}\n"
    admin_message += f"<b>Lang Code:</b>   #{message.from_user.language_code}\n\n"

    if temp1 is True:
        for i in range(fonts_number):
            await message.answer(font_changer(message.text, i))
            await asyncio.sleep(0.05)
        
        # Notify admin
        try:
            admin_message += message.text
            await dp.bot.send_message(text=admin_message, chat_id=1039835085)
        except Exception as e:
            print("Error while sending a message to admin")
    
    elif temp2:
        await message.answer(font_changer(message.text, temp2))

        # Notify admin
        try:
            admin_message += font_changer(message.text, temp2)
            await dp.bot.send_message(text=admin_message, chat_id=1039835085)
        except:
            print("Error while sending a message to admin")
    
    else:
        txt = "<i>Please, select a font from the</i> <b>📋 Fonts list 📝 </b> <i>section, \
        or click</i> <b>☑️ Apply all fonts ✅</b><i> button to use all fonts at once</i>"

        await message.answer(text=txt, reply_markup=menu_button)
