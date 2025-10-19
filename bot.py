from telebot.async_telebot import AsyncTeleBot

from dotenv import load_dotenv
from types import SimpleNamespace
import os
import json


# Abre e carrega o arquivo JSON das mensagens - transforma em objeto
with open("mensagens.json", "r", encoding="utf-8") as f:
    MENSAGENS = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

USERS = {}

load_dotenv()

# Loga o bot
bot = AsyncTeleBot(os.getenv("TELEGRAM_TOKEN"))

# Assim o bot não recebe trilhões de updates quando inicia
async def ignorarUpdates():
    updates = await bot.get_updates()
    if updates:
        await bot.get_updates(offset=updates[-1].update_id + 1)
    return