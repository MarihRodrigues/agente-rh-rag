# Agente de Automação de RH com RAG

Projeto em Python capaz de ler um documento de RH e responder perguntas usando apenas as informações encontradas na base documental.

## Tecnologias
- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Ollama
- RAG (Retrieval-Augmented Generation)

## Como funciona

1. O sistema lê os arquivos PDF da pasta `documentos`.
2. O conteúdo é dividido em pequenos trechos.
3. Cada trecho é transformado em embeddings.
4. Os embeddings são armazenados no ChromaDB.
5. Quando o usuário faz uma pergunta, o sistema busca os trechos mais relevantes.
6. A pergunta e os trechos encontrados são enviados para o modelo local.
7. O sistema responde apenas com base no contexto encontrado.

## Instalação

### 1. Criar ambiente virtual

```powershell
python -m venv .venv
```

### 2. Ativar

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 4. Instalar o Ollama

Instale o Ollama e baixe um modelo, por exemplo:

```powershell
ollama pull llama3.2:3b
```

Depois deixe o Ollama em execução.

### 5. Configurar variáveis

Copie `.env.example` para `.env`.

### 6. Executar

```powershell
python main.py
```

## Exemplos de perguntas

- Quantos dias de férias o colaborador possui?
- Com quanto tempo de antecedência devo solicitar férias?
- Como funciona o trabalho remoto?
- Quais benefícios são oferecidos?
- O que devo fazer se estiver doente?
- Qual é a política de confidencialidade?

## Estrutura

```text
agente-rh-rag/
├── documentos/
│   └── manual_rh.txt
├── src/
│   ├── config.py
│   ├── carregar_documentos.py
│   ├── criar_base.py
│   └── agente_rh.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```
