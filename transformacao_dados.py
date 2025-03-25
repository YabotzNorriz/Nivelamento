import zipfile
import pdfplumber
import pandas as pd

ARQUIVO_PDF = "resources/anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

ARQUIVO_CSV = "Resources/Rol_de_Procedimentos_e_Eventos.csv"

mapa_OD = {"OD": "Ordem de Despesa"}
mapa_AMB = {"AMB": "Ambulatorial"}

dados_processados = []
header = None

try:
    with pdfplumber.open(ARQUIVO_PDF) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()
            for linha in tabelas:
                if linha and len(linha) > 0:
                    if header is None:
                        header = linha[0]
                        dados_processados.extend(linha)
                    else:
                        if linha[0] == header:
                            dados_processados.extend(linha[1:])
                        else:
                            dados_processados.extend(linha)

    if header is None:
        print("Nenhum dado extraído do PDF.")
    else:
        data_frame = pd.DataFrame(dados_processados[1:], columns=header)

        if "OD" in data_frame.columns:
            data_frame["OD"] = data_frame["OD"].replace(mapa_OD)
        if "AMB" in data_frame.columns:
            data_frame["AMB"] = data_frame["AMB"].replace(mapa_AMB)

        data_frame.to_csv(ARQUIVO_CSV, index=False, encoding="utf-8")
        print("Dados extraídos e salvos com sucesso em: " + ARQUIVO_CSV)

    arquivo_compactado = "Teste_JoaoPedroAndradePaesPimentelBarbosa.zip"
    with zipfile.ZipFile(arquivo_compactado, "w") as zip:
        zip.write(ARQUIVO_CSV)
    print(arquivo_compactado + " criado com sucesso!")
except PermissionError as e:
    print(e)
