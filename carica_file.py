import oci

config = oci.config.from_file()
object_storage = oci.object_storage.ObjectStorageClient(config)

namespace = "axme5c5goo9t"
bucket = "gpini-python-cloud-storage"

# inviamo una richiesta HTTP a Oracle per il caricamento e salviamo la risposta in risultato
with open("documento.txt", "rb") as file:
    risultato = object_storage.put_object(
        namespace_name=namespace,
        bucket_name=bucket,
        object_name="documento.txt", #nome che avrà su Oracle
        put_object_body=file
    )

print("File caricato correttamente!")
print("Codice HTTP:", risultato.status)