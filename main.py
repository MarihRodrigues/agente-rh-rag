from src.agente_rh import AgenteRH
from src.criar_base import criar_base, carregar_base_existente


def main():
    print("=" * 60)
    print("AGENTE DE AUTOMACAO DE RH")
    print("=" * 60)

    print("\nVerificando base de conhecimento...")
    base = carregar_base_existente()

    if base is None:
        print("Base nao encontrada. Criando base pela primeira vez...")
        base = criar_base()
    else:
        print("Base encontrada e carregada.")

    agente = AgenteRH(base)
    print("\nAgente pronto!")
    print("Digite sua pergunta sobre o manual de RH.")
    print("Digite 'sair' para encerrar.")
    print("Digite 'recriar' para atualizar a base apos alterar documentos.\n")

    while True:
        pergunta = input("Voce: ").strip()
        if not pergunta:
            continue
        if pergunta.lower() == "sair":
            print("\nAgente: Ate logo!")
            break
        if pergunta.lower() == "recriar":
            print("\nRecriando a base de conhecimento...")
            base = criar_base()
            agente = AgenteRH(base)
            print("Base atualizada com sucesso!\n")
            continue
        try:
            resposta = agente.responder(pergunta)
            print(f"\nAgente RH: {resposta}\n")
        except Exception as erro:
            print(f"\nErro ao responder: {erro}\n")
            print("Verifique se o Ollama esta instalado, em execucao e se o modelo foi baixado.\n")


if __name__ == "__main__":
    main()
