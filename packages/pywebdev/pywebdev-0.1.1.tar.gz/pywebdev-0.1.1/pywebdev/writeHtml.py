import os

# No arquivo writeHtml.py

def locateHtml(arquivo):
    # Função para localizar o arquivo HTML no diretório atual
    return os.path.join(os.getcwd(), arquivo)

def writeTop(titulo, css_filename):
    arquivo_html = locateHtml("index.html")
    with open(arquivo_html, 'w', encoding='utf-8') as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write(f"  <title>{titulo}</title>\n")
        file.write("  <meta charset='UTF-8'>\n")
        file.write(f"  <link rel='stylesheet' type='text/css' href='{css_filename}'>\n")  # Adicione o link para o CSS
        # Adicione aqui quaisquer outros elementos do cabeçalho (head) que você desejar
        file.write("</head>\n")
        file.write("<body>\n")

def writeCenter(codigo):
    arquivo_html = locateHtml("index.html")
    with open(arquivo_html, 'a', encoding='utf-8') as file:
        file.write(f"  <div id='center'>{codigo}</div>\n")

def writeEnd():
    arquivo_html = locateHtml("index.html")
    with open(arquivo_html, 'a', encoding='utf-8') as file:
        file.write("</body>\n")
        file.write("</html>\n")
