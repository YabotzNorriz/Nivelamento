from PyPDF2 import PdfReader
import pandas as pd

ARQUIVO_PDF = "anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
dados_extraidos = []

try:
    reader = PdfReader(ARQUIVO_PDF)

    for pagina in reader.pages:
        texto = pagina.extract_text()
        if texto.strip():
            linhas = texto.split("\n")
            for linha in linhas:
                dados_extraidos.append(linha.strip())

    data_frame = pd.DataFrame(dados_extraidos, columns=["Dados brutos"])

    data_frame_limpo = data_frame["Dados brutos"].str.split(";", expand=True)
    data_frame_limpo.columns = [
        "Coluna 1",
        "Coluna 2",
        "Coluna 3",
        "Coluna 5",
        "Coluna 5",
    ]

    arquivo_csv = "saida.csv"
    data_frame_limpo.to_csv(arquivo_csv, index=False, encoding="utf-8")
    print("Arquivo: " + arquivo_csv)

except IOError as e:
    print("Ocorreu um erro: " + e)
