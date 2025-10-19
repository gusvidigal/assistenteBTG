from telebot.formatting import format_text, mbold, escape_markdown
from bot import bot

# Comandos
async def ping(msg):
    await bot.send_message(chat_id=msg.chat.id,parse_mode="MarkdownV2", 
                           text=format_text(escape_markdown("Pong!")))
    return
async def ajuda(msg):
    await bot.send_message(chat_id=msg.chat.id,parse_mode="MarkdownV2",
                            text=format_text(mbold("Placar geral:\n"), separator=""))
    return


