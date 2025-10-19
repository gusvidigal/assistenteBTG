import asyncio
from bot import USERS, MENSAGENS, bot, ignorarUpdates
from metas import detectarIntencaoViagem, handlerMensagemMetas
import comandos
import funcoes

# Registra os comandos
bot.register_message_handler(comandos.ajuda, commands=['ajuda'])

@bot.message_handler(func=lambda msg: True)
async def handlerMsg(mensagem):
    # Se for mensagem de ajuda
    if funcoes.formatMsg(mensagem.any_text) == "ajuda":
        await comandos.ajuda(mensagem)
        return

    userID = mensagem.from_user.id
    chatID = mensagem.chat.id
    texto = mensagem.text or ""

    # Se já estiver no fluxo de viagem, continua sem detectar intenção
    if userID in USERS and USERS[userID].get("in_viagem_flow", False):
        await handlerMensagemMetas(userID, chatID, texto)
        return

    # Detecta intenção de viagem
    if await detectarIntencaoViagem(texto):
        USERS[userID] = {
            "conversation": texto,
            "destino": None,
            "orcamento": None,
            "prazo_meses": None,
            "stage_confirm": False,
            "in_viagem_flow": True
        }
        await handlerMensagemMetas(userID, chatID, texto)
    else:
        await bot.send_message(chatID, MENSAGENS.INTERACAO_INVALIDA)



# Executa o programa
async def main():
    await ignorarUpdates()
    print("Bot (cronicamente) online!")
    await bot.polling(non_stop=True)

if __name__ == "__main__":
    asyncio.run(main())