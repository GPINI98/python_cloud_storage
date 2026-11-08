import oci

config = oci.config.from_file()
oci.config.validate_config(config)

identity = oci.identity.IdentityClient(config)
utente = identity.get_user(config["user"]).data

print("Connessione Oracle riuscita!")
print("Utente:", utente.name)