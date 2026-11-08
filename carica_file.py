from storage import carica_file

risultato = carica_file("documento.txt")
# risultato = carica_file("inesistente.pdf")

if risultato == 200:
    print("Caricamento completato!")
elif risultato is None:
    print("File non trovato.")
else:
    print("Caricamento non riuscito. Codice:", risultato)