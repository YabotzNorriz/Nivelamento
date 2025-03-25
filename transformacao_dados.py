from PyPDF2 import PdfReader
import csv

arquivo_pdf = "anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
arquivo_csv = "saida.csv"

try:
    reader = PdfReader(arquivo_pdf)

    with open(arquivo_csv, mode="w", newline="", encoding="utf-8") as file_csv:
        writer_csv = csv.writer(arquivo_csv)

        for pagina in reader.pages:
            texto = pagina.extract_text()
            if texto:
                linhas = texto.split("\n")
                for linha in linhas:
                    writer_csv.writerow([linha])

    print("Dados salvos em: " + arquivo_csv)

except IOError as e:
    print("Ocorreu um erro: " + e)
