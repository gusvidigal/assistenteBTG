# Assistente Virtual BTG
Bot no telegram para o Hackaton da Semcomp+BTG de 2025

## Introdução
Nós somos o grupo "Os 3 Computeiros" e queremos propor funcionalidades novas para o Assistente Virtual da BTG, no Whatsapp.

Membros do grupo:
- Gustavo Vidigal Schulgin
- João Pedro Boiago Gomes Santana
- Lorena Moreira Borges
- Rafaela Dâmaso Breseghello

Percebemos que o Assistente Virtual da BTG no Whatsapp é uma ferramenta muito poderosa para facilitar e descomplicar a vida dos brasileiros, uma vez que torna mais prático o processo de realização de pagamentos bancários e gestão pessoal de finanças - sem afetar a segurança ou a qualidade da experiência do usuário.

Porém, como a ferramenta ainda está em desenvolvimento, propomos ideias para tornar o Assistente mais completo e intuitivo.

## Jornada do Cliente

Muitos clientes, por medo, utilizam o aplicativo do banco em um celular à parte, uma vez que deixá-lo no seu celular principal pode ser bastante perigoso em casos de assalto, por exemplo. Por isso, o Assistente no Whatsapp acaba sendo um facilitador das funções já presentes no aplicativo.

Mas e se ele deixasse de ser um facilitador e se tornasse um ambiente financeiro completo para o cliente?

Isso é possível integrando LLMs no bot, a fim de transformar uma sequência de comandos e ações em uma conversa casual com uma pessoa - nesse caso, o Assistente Virtual do BTG.

Tudo começa no vínculo da conta no Whatsapp com o aplicativo do banco e o aceite dos termos de uso do bot. A segurança não fica comprometida, porque, em versões recentes do Whatsapp, é possível proteger a rede por biometria (e até restringir o uso aos usuários que a possuem ativada).

Depois desse cadastro, o bot se introduz e explica algumas funcionalidades, além de perguntar se o usuário deseja realizar a configuração completa do sistema.

Caso ele não queira, simples! As funcionalidades são introduzidas gradativamente ao longo do uso, por meio de dicas e sugestões do bot, mandadas após cada grande interação.

A partir daqui, o usuário fica livre para conversar a qualquer momento com a LLM do bot, que identificará a intenção e a ação a ser executada e responderá em conformidade.

Dividimos as funcionalidades do bot em 4 áreas principais:

### 1. Serviços básicos
Corresponde às funções já implementadas pelo Assistente Virtual da BTG, além de ações que também já possuem implementação no bot, mas que não foram ativadas pelo usuário ainda. Nesse caso, o bot o orientará a permitir essa ação pelo aplicativo do banco (por exemplo, aumentar o limite do pix noturno!).

### 2. Análise de consumo
Corresponde a funções relacionadas à interpretação do consumo do usuário, como geração de relatórios de consumo, comparações, balancetes, gastos mensais e identificação de padrões para pagamentos automáticos.

### 3. Análise de investimentos
Aqui, inovamos ao trazer funções de investimentos ao bot. O bot determina, logo no vínculo da conta, se ele já assinou o Termo de Adesão a Investimentos no aplicativo. Além disso, ele realiza um quiz com o usuário para traçar um perfil de investidor e orientar próximas ações.

O usuário pode se inscrever em newsletters sobre investimentos no Whatsapp, pedir sugestões de investimentos e realizar simulações de renda fixa.

### 4. Estabelecimento e metas
Também uma funcionalidade nova: O usuário pode definir metas e o bot pode acompanhá-las e sugerir ações com base no perfil de consumo. As metas são divididas em 3 categoriais: obter uma quantia de dinheiro em um prazo, comprar algum item/imóvel ou viajar. O bot conversará com o usuário a fim de obter mais informações a respeito dessa meta e, a partir daí, montará um cronograma de metas parciais.

A cada vencimento desses prazos ou cumprimento dessas metas parciais, o bot reajustará o cronograma, se necessário, sugerirá investimentos bastante relevantes para atingir o objetivo e fornecerá um panorama do progresso para atingir o objetivo.

O cadastro de uma meta relacionada à viagem está implementada no bot.

## Fluxograma da Jornada do Cliente
Pode ser acessado por meio desse link:

## Instalação
Pré-requisitos:

- `Python 3` com o pacote [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/index.html)

## Execução
Basta utilizar o comando `make run` para executar o bot. Uma mensagem será impressa no terminal quando ele estiver online.
