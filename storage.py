import oci
from pathlib import Path

#lazy initialization
def crea_client_storage():
    config = oci.config.from_file()
    return oci.object_storage.ObjectStorageClient(config)

NAMESPACE = "axme5c5goo9t"
BUCKET = "gpini-python-cloud-storage"

def carica_file(percorso_file):
    nome_file = Path(percorso_file).name #estrae solo il nome esaminando il percorso

    try:
        client = crea_client_storage()
        with open(percorso_file, "rb") as file:
            risultato = client.put_object(
                namespace_name=NAMESPACE,
                bucket_name=BUCKET,
                object_name=nome_file,
                put_object_body=file
            )
        return risultato.status
    
    except FileNotFoundError: #errore se il file non esiste
        return None

    except oci.exceptions.ServiceError as errore: #as errore assegna l'errore alla variabile errore
        print("Errore Oracle:", errore.message) #errore restituito da Oracle
        return None

def lista_file():
    try:
        client = crea_client_storage()
        risultato = client.list_objects(
            namespace_name=NAMESPACE,
            bucket_name=BUCKET
        )

        oggetti = risultato.data.objects
        nomi_file = []

        for oggetto in oggetti:
            nomi_file.append(oggetto.name)

        return nomi_file

    except oci.exceptions.ServiceError as errore:
        print("Errore Oracle:", errore.message)
        return None

def scarica_file(nome_file, percorso_destinazione):
    try:
        client = crea_client_storage()
        risultato = client.get_object( #richiesta
            namespace_name=NAMESPACE,
            bucket_name=BUCKET,
            object_name=nome_file,
        )
    
        with open(percorso_destinazione, "wb") as file: 
            file.write(risultato.data.content) #scrittura dati

        return risultato.status

    except FileNotFoundError: #errore se il file non esiste
        return None

    except oci.exceptions.ServiceError as errore: 
        if errore.status == 404:
            print("Oggetto non trovato su Oracle.")
        else:
            print("Errore Oracle:", errore.message)
        return None