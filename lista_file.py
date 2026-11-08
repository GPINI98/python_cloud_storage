from storage import lista_file

risultato = lista_file()

if risultato is None:
    print("Impossibile recuperare i file.")
elif risultato:
    for nome in risultato:
        print(nome)
else:
    print("Il bucket è vuoto.")