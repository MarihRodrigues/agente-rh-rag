from langchain_community.document_loaders import PyPDFLoader, TextLoader

from src.config import DOCUMENTOS_DIR


def carregar_documentos():
    documentos = []

    arquivos = list(DOCUMENTOS_DIR.glob("*.txt")) + list(DOCUMENTOS_DIR.glob("*.pdf"))

    if not arquivos:
        raise FileNotFoundError(
            f"Nenhum arquivo .txt ou .pdf foi encontrado em: {DOCUMENTOS_DIR}"
        )

    for arquivo in arquivos:
        print(f"Lendo: {arquivo.name}")

        if arquivo.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(arquivo))
        else:
            loader = TextLoader(str(arquivo), encoding="utf-8")

        documentos.extend(loader.load())

    return documentos
