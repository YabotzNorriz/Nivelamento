import pdfplumber
import pandas as pd


arquivo_pdf = "anexos/Anexo_I_teste.pdf"

tabelas_extraidas = []

try:
    with pdfplumber.open(arquivo_pdf) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                tabelas_extraidas.extend(tabela)

    data_frame = pd.DataFrame(tabelas_extraidas)

    arquivo_excel = "tabelas_extraidas.xlsx"
    data_frame.to_excel(arquivo_excel, index=False, header=False)

    data_frame = pd.read_excel(arquivo_excel, header=None)
    data_frame.columns = data_frame.iloc[0]
    data_frame = data_frame[1:]

    arquivo_csv = "tabela_normalizada.csv"
    data_frame.to_csv(arquivo_csv, index=False, encoding="utf-8")

except PermissionError as e:
    print(f"Ocorreu um erro ao processar o PDF: {e}")
