from storage import scarica_file

risultato = scarica_file(
    # "file_inesistente.txt", "download.txt"
    "documento.txt",
    "documento_scaricato.txt"
)

if risultato == 200:
    print("Download completato!")