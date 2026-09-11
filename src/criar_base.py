import shutil

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.carregar_documentos import carregar_documentos
from src.config import CHROMA_DIR


def obter_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def criar_base():
    documentos = carregar_documentos()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
    )

    chunks = splitter.split_documents(documentos)

    if CHROMA_DIR.exists():
        shutil.rmtree(CHROMA_DIR)

    embeddings = obter_embeddings()

    banco = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    print("Base criada com sucesso.")
    print(f"Documentos carregados: {len(documentos)}")
    print(f"Trechos criados: {len(chunks)}")

    return banco


def carregar_base_existente():
    if not CHROMA_DIR.exists():
        return None

    embeddings = obter_embeddings()

    return Chroma(
        persist_directory=str(CHROMA_DIR),
        embedding_function=embeddings,
    )
