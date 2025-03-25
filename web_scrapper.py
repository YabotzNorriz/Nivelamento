import os
import zipfile
import requests
from bs4 import BeautifulSoup

URL_SITE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"


def identificar_extensao_arquivo(nome_arquivo):
    _, extensao = os.path.splitext(nome_arquivo)
    return extensao.lower()


def obter_nome_arquivo(response, url):
    if "Content-Disposition" in response.headers:
        conteudo_header = response.headers["Content-Disposition"]
        if "filename=" in conteudo_header:
            return conteudo_header.split("filename=")[-1].strip('"')
    return url.split("/")[-1]


try:
    response = requests.get(URL_SITE)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    file_links = soup.find_all("a", href=True)
    arquivos = []
    for link in file_links:
        if "Anexo" in link.text:
            arquivos.append(link["href"])
    print(f"Links encontrados: {arquivos}")

    arquivos_encontrados = []
    for i, file_url in enumerate(arquivos):
        response = requests.get(file_url)
        response.raise_for_status()

        nome_arquivo = obter_nome_arquivo(response, file_url)
        with open(nome_arquivo, "wb") as arquivo:
            arquivo.write(response.content)
        print(nome_arquivo + " baixado com sucesso!")

        extensao_arquivo = identificar_extensao_arquivo(nome_arquivo)
        if "pdf" in nome_arquivo:
            arquivos_encontrados.append(nome_arquivo)
            pasta = "../anexos"
            os.makedirs(pasta, exist_ok=True)
            path_completo = os.path.join(pasta, nome_arquivo)

            with open(path_completo, "w") as arquivo:
                arquivo.write(nome_arquivo)
        else:
            os.remove(nome_arquivo)
            print("Arquivo removido: " + nome_arquivo + "\ntipo" + extensao_arquivo)

    arquivo_compactado = "anexos.zip"
    with zipfile.ZipFile(arquivo_compactado, "w") as zip:
        for arquivo in arquivos_encontrados:
            zip.write(arquivo)
    print(arquivo_compactado + " criado com sucesso!")

    for nome_arquivo in arquivos_encontrados:
        os.remove(nome_arquivo)
    print("Os arquivos originais foram removidos")

except requests.exceptions.RequestException as e:
    print("Ocorreu um erro " + e)
