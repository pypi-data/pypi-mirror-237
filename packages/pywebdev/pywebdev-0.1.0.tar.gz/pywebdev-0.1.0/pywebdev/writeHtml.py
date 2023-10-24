import os
from . import locateHtml

def writeTop(titulo, nome_arquivo):
    """
    Cria a parte superior de um arquivo HTML, incluindo o DOCTYPE, cabeçalho e início do corpo, e escreve-o no arquivo especificado.

    Args:
        titulo (str): O título da página HTML.
        nome_arquivo (str): O nome do arquivo HTML a ser criado e escrito.

    Returns:
        bool: True se a operação for bem-sucedida, False em caso de erro.
    """
    html_top = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{titulo}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Adicione mais metatags ou links CSS aqui, se necessário -->
</head>
<body>
"""
    try:
        with open(locateHtml(nome_arquivo), 'w', encoding='utf-8') as arquivo:
            arquivo.write(html_top)
        return True
    except Exception as e:
        print(f"Erro ao escrever o arquivo HTML: {str(e)}")
        return False

def writeCenter(codigo, nome_arquivo):
    """
    Cria a seção central do código HTML e escreve-a no arquivo especificado.

    Args:
        codigo (str): O código HTML que deve ser colocado no centro do HTML.
        nome_arquivo (str): O nome do arquivo HTML a ser criado e escrito.

    Returns:
        bool: True se a operação for bem-sucedida, False em caso de erro.
    """
    html_center = f"""<div id="center">
    {codigo}
</div>
"""
    try:
        with open(locateHtml(nome_arquivo), 'w', encoding='utf-8') as arquivo:
            arquivo.write(html_center)
        return True
    except Exception as e:
        print(f"Erro ao escrever o arquivo HTML: {str(e)}")
        return False

def writeEnd(nome_arquivo):
    """
    Finaliza o corpo e o HTML no arquivo especificado.

    Args:
        nome_arquivo (str): O nome do arquivo HTML a ser escrito.

    Returns:
        bool: True se a operação for bem-sucedida, False em caso de erro.
    """
    html_end = """</body>
</html>
"""
    try:
        with open(locateHtml(nome_arquivo), 'w', encoding='utf-8') as arquivo:
            arquivo.write(html_end)
        return True
    except Exception as e:
        print(f"Erro ao escrever o arquivo HTML: {str(e)}")
        return False
