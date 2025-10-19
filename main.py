import asyncio
import comandos
from bot import bot

# Registra os comandos
bot.register_message_handler(comandos.ping, commands=['ping'])
bot.register_message_handler(comandos.ajuda, commands=['ajuda'])


# Assim o bot não recebe trilhões de updates quando inicia
async def ignorarUpdates():
    updates = await bot.get_updates()
    if updates:
        await bot.get_updates(offset=updates[-1].update_id + 1)

# Coloca o bot online
asyncio.run(ignorarUpdates())
print("Bot (cronicamente) online!")
asyncio.run(bot.polling())