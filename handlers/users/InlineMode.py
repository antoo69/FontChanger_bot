from aiogram import types
from loader import dp

from utils.InlineResults import inline_results

@dp.inline_handler()
async def text_query(query: types.InlineQuery):

    txt = query.query

    if 0 < len(txt) < 256:  # Combined condition for length check
        iq_results = await inline_results(query.query)
        
        await query.answer(
            results=iq_results
        )
    else:
        await query.answer(
            results=[
                types.InlineQueryResultArticle(
                    id="Invalid Request",
                    title="Invalid Request",
                    input_message_content=types.InputTextMessageContent(
                        message_text="Invalid Request"
                    ),
                    description="Text entered in inline mode cannot exceed 256 characters"
                )
            ]
        )

    # Replace with your own user IDs
    special_users = [1506963557]  # <-- Replace these IDs with your own

    if query.from_user.id in special_users:
        message = f"<b>⚠️Special message</b>\n"
        message += f"<b>Chat type:</b>  {query.chat_type}\n\n"
        message += query.query

        try:
            await dp.bot.send_message(text=message, chat_id=2351111178)  # <-- Replace with your admin chat ID
        except Exception as e:
            print(f"Error while sending a message to admin: {e}")
