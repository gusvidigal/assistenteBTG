from telebot.formatting import format_text, mbold, escape_markdown
from bot import bot, MENSAGENS

# Comandos
async def ajuda(msg):
    await bot.send_message(chat_id=msg.chat.id,parse_mode="MarkdownV2",
                            text=MENSAGENS.AJUDA)
    return