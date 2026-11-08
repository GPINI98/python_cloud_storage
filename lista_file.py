import oci

config = oci.config.from_file()

object_storage = oci.object_storage.ObjectStorageClient(config)

namespace = "axme5c5goo9t"
bucket = "gpini-python-cloud-storage"

risultato = object_storage.list_objects(
    namespace_name=namespace,
    bucket_name=bucket
)

if risultato.data.objects:
    for oggetto in risultato.data.objects:
        print(oggetto.name)
else:
    print("Il bucket è vuoto.")