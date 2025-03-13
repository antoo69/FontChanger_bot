import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from loader import bot


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
            if update.message.text in ['/start', '/help']:
                return
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        
        logging.info(f"User ID: {user}")  # Log hanya ID user tanpa cek fsub

        # Tidak ada forced sub, langsung lanjut
        return  
