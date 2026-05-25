# 🌤️ ClimIA — Assistente Inteligente de Clima

Aplicação desenvolvida como projeto final da matéria de Programação Aplicada em Python do curso de Especialização Técnica em Desenvolvimento de Aplicações para Inteligência Artificial do SENAI, integrando Python, APIs, JSON, automação com n8n e Inteligência Artificial.

## 📋 Descrição

O ClimIA é um assistente de clima via terminal que consulta dados meteorológicos em tempo real, salva um histórico de consultas e envia uma mensagem inteligente gerada por IA direto no Telegram do usuário.

## 🚀 Tecnologias Utilizadas

- Python 3.12
- [OpenWeatherMap API](https://openweathermap.org/) — dados meteorológicos
- [n8n](https://n8n.io/) — automação de workflows
- [Groq API](https://groq.com/) — geração de mensagens com IA (modelo LLaMA)
- [Telegram Bot API](https://core.telegram.org/bots/api) — envio de mensagens
- Bibliotecas Python: `requests`, `python-dotenv`

## 🔄 Fluxo do Sistema

```
Usuário → Python → OpenWeatherMap API → n8n Webhook → Groq (IA) → Telegram
```
<img width="1478" height="535" alt="dashbord_n8n" src="https://github.com/user-attachments/assets/dbb19cf6-1823-46ba-ba0f-9a2cb4b36158" />
<img width="1170" height="604" alt="code_n8n" src="https://github.com/user-attachments/assets/f9b4506f-22c3-4b6f-98d0-55065c2aa320" />
<img width="1546" height="311" alt="resultado_ia_n8n" src="https://github.com/user-attachments/assets/bb83b89a-abff-4fb5-be52-1fa8ea1fe44e" />




## 📁 Estrutura de Arquivos

```
Projeto_ClimIA/
│
├── main.py              # Arquivo principal — menu e lógica de consulta
├── historico.py         # Função de salvamento do histórico em JSON
├── notificacao.py       # Função de envio para o Webhook do n8n
├── .env.example         # Modelo de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Documentação do projeto
```

## ⚙️ Como Instalar e Configurar

**1. Clone o repositório**
```bash
git clone git@github.com:dvbcknd/Projeto_ClimIA.git
cd Projeto_ClimIA
```

**2. Crie e ative o ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install requests python-dotenv
```

**4. Configure as variáveis de ambiente**

Copie o arquivo de exemplo e preencha com suas chaves:
```bash
cp .env.example .env
```

```
API_KEY=sua_chave_openweathermap
WEBHOOK_URL=sua_url_webhook_n8n
```

**5. Inicie o n8n**
```bash
n8n start
```

## ▶️ Como Usar

Execute o programa no terminal:
```bash
python3 main.py
```

O menu vai aparecer com as opções:
- **1** — Pesquisar clima de uma cidade
- **2** — Ver histórico de consultas
- **3** — Sair do programa

A cada consulta, uma mensagem gerada por IA será enviada automaticamente para o Telegram.

## 📊 Requisitos do Projeto Atendidos

| Requisito | Status |
|---|---|
| Entrada de dados com `input()` | ✅ |
| Estruturas condicionais `if/elif/else` | ✅ |
| Estruturas de repetição `while` | ✅ |
| Funções personalizadas | ✅ |
| Manipulação de arquivos `.json` | ✅ |
| Consumo de APIs HTTP | ✅ |
| Integração com n8n | ✅ |
| Integração com IA (Groq/LLaMA) | ✅ |

## 👨‍💻 Autor

Bruno — Curso de  Especialização Técnica em Desenvolvimento de Aplicações para Inteligência Artificialdo SENAI Bahia
