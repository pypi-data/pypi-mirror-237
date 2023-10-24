import os

def locateHtml(arquivo):
    """
    Localiza um arquivo no mesmo diretório do script Python.

    Args:
        arquivo (str): O nome do arquivo a ser localizado.

    Returns:
        str: O caminho completo para o arquivo.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    arquivo_path = os.path.join(script_dir, arquivo)
    return arquivo_path
