from telebot.formatting import format_text, mbold, escape_markdown
import unicodedata
import re

# Extrai caracteres especiais da mensagem
def formatMsg(msg):
    msg = msg.lower()
    msg = unicodedata.normalize('NFD', msg)

    # Remove diacríticos
    msg = ''.join(
        c for c in msg
        if unicodedata.category(c) != 'Mn'
    )
    msg = re.sub(r'[^a-z\s]', '', msg)
    msg = re.sub(r'\s+', ' ', msg).strip()
    
    return msg

# Substitui placeholders %% (para os JSON de prompts)
def placeHolder(texto, *argumentos):
    resultado = texto
    for value in argumentos:
        resultado = resultado.replace("%%", str(value), 1)  # substitui uma ocorrência por vez
    return resultado
