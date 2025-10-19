import random
from bot import USERS, MENSAGENS, bot
from gemini import promptGemini, PROMPTS
from funcoes import placeHolder

CAMPOS = ["destino", "orcamento", "prazo_meses"]

# Obtém as dicas
with open("Utilidades/dicas.txt", "r", encoding="utf-8") as f:
    DICAS = f.read().split("\n")

# Detecta se o usuário quer planejar uma viagem
async def detectarIntencaoViagem(texto):
    prompt = placeHolder(PROMPTS.metas.viagens.INTENCAO_VIAGEM, texto)
    resposta = await promptGemini(prompt, max_tokens=20)
    return resposta.strip().lower() in ("sim", "yes")


# Passa para o próximo campo faltante
def proximoCampo(state):
    for f in CAMPOS:
        if state.get(f) is None:
            return f
    return None


# Gerencia a lógica da conversa
async def handlerMensagemMetas(userID, chatID, texto):
    # Cria estado se necessário
    if userID not in USERS:
        USERS[userID] = {
            "conversation": "",
            "destino": None,
            "orcamento": None,
            "prazo_meses": None,
            "stage_confirm": False,
            "in_viagem_flow": False
        }

    state = USERS[userID]
    state["conversation"] += "\n" + texto

    # Preenche campos faltantes com LLM
    for field in CAMPOS:
        if state[field] is None:
            value = await requererCampo(state["conversation"], field)
            if value is not None:
                state[field] = value

    # Verifica se ainda falta algum campo
    missing = proximoCampo(state)
    if missing:
        perguntas = {
            "destino": MENSAGENS.metas.CAMPO_DESTINO,
            "orcamento": MENSAGENS.metas.CAMPO_ORCAMENTO,
            "prazo_meses": MENSAGENS.metas.CAMPO_PRAZO
        }
        await bot.send_message(chatID, perguntas[missing])
        return

    # Todos os campos preenchidos → pede confirmação
    if not state["stage_confirm"]:
        d, o, p = state["destino"], state["orcamento"], state["prazo_meses"]
        mensagem = placeHolder(MENSAGENS.metas.CONFIRMACAO, d, int(o),p)

        await bot.send_message(chatID, mensagem)
        state["stage_confirm"] = True
        return

    # Usuário confirma
    if texto.strip().lower() in ("sim", "s"):
        await bot.send_message(chatID, MENSAGENS.metas.GERANDO_PLANO)
        plano = await gerarPlano(state)
        await bot.send_message(chatID, plano)

        # Envia uma dica aleatória
        dica = random.choice(DICAS)
        await bot.send_message(chatID, dica)

        # Reseta estado
        USERS[userID] = {
            "conversation": "",
            "destino": None,
            "orcamento": None,
            "prazo_meses": None,
            "stage_confirm": False,
            "in_viagem_flow": False
        }

    elif texto.strip().lower() in ("não", "nao", "n"):
        USERS[userID] = {
            "conversation": "",
            "destino": None,
            "orcamento": None,
            "prazo_meses": None,
            "stage_confirm": False,
            "in_viagem_flow": False
        }
        await bot.send_message(chatID, MENSAGENS.metas.INICIAL)

    else:
        if state["stage_confirm"]:
            await bot.send_message(chatID, MENSAGENS.metas.S_N)


# Extrai valor de um campo específico
async def requererCampo(conversa, campo):
    if campo == "destino":
        prompt = placeHolder(PROMPTS.metas.viagens.CAMPO_DESTINO, conversa)
    elif campo == "orcamento":
        prompt = placeHolder(PROMPTS.metas.viagens.CAMPO_ORCAMENTO, conversa)
    elif campo == "prazo_meses":
        prompt = placeHolder(PROMPTS.metas.viagens.CAMPO_PRAZO, conversa)
    else:
        return None

    textoBruto = (await promptGemini(prompt)).strip().lower()
    if textoBruto in ("null", ""):
        return None

    try:
        if campo == "orcamento":
            textoBruto = textoBruto.replace(".", "").replace(",", "")
            if textoBruto.endswith("k"):
                return float(textoBruto[:-1]) * 1000
            return float(textoBruto)
        elif campo == "prazo_meses":
            return int(float(textoBruto))
        else:
            return textoBruto.strip().capitalize()
    except:
        return None


# Gera um cronograma final
async def gerarPlano(dados):
    prompt = placeHolder(PROMPTS.metas.viagens.PLANO_FINAL, 
                         dados['destino'],dados['orcamento'],dados['prazo_meses'])
    return await promptGemini(prompt, 400)

