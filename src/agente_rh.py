from langchain_ollama import ChatOllama
from src.config import OLLAMA_BASE_URL, OLLAMA_MODEL

class AgenteRH:
    def __init__(self, vectorstore):
        self.vectorstore = vectorstore
        self.llm = ChatOllama(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, temperature=0)

    def responder(self, pergunta):
        documentos = self.vectorstore.similarity_search(pergunta, k=4)
        contexto = "\n\n---\n\n".join(documento.page_content for documento in documentos)
        prompt = f'''Voce e um assistente de Recursos Humanos.

Responda SOMENTE usando as informacoes presentes no CONTEXTO abaixo.

REGRAS:
1. Nao invente informacoes.
2. Nao use conhecimentos externos.
3. Se a resposta nao estiver no contexto, responda: "Nao encontrei essa informacao no manual de RH disponivel."
4. Responda em portugues do Brasil.
5. Seja claro e objetivo.

CONTEXTO:
{contexto}

PERGUNTA:
{pergunta}

RESPOSTA:
'''
        resposta = self.llm.invoke(prompt)
        return resposta.content
