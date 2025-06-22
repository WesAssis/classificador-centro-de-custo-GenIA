def carregar_prompt(caminho_arquivo):
    """
    Lê o conteúdo de um arquivo de prompt e retorna como string.
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return f.read()
