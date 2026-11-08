from unittest.mock import patch, Mock #libreria python per simulare Oracle
from storage import carica_file, lista_file
import oci

                            # tmp_path cartella temporanea
def test_carica_file_successo(tmp_path):
    percorso_file = tmp_path / "documento.txt"
    percorso_file.write_text("Contenuto di prova")

    risposta = Mock() # simula un oggetto
    risposta.status = 200

    with patch("storage.object_storage.put_object", return_value=risposta):
        risultato = carica_file(percorso_file)
    assert risultato == 200


def test_carica_file_non_trovato(tmp_path):
    percorso_file = tmp_path / "inesistente.txt"

    with patch("storage.object_storage.put_object") as mock_upload:
        risultato = carica_file(percorso_file)
    assert risultato is None
    mock_upload.assert_not_called() #caricamento mai avviato


def test_carica_file_errore_oracle(tmp_path):
    percorso_file = tmp_path / "documento.txt"
    percorso_file.write_text("Contenuto di prova")

    errore = oci.exceptions.ServiceError(
        status=500,
        code="InternalError",
        headers={},
        message="Errore simulato"
    )

    with patch("storage.object_storage.put_object", side_effect=errore):
        risultato = carica_file(percorso_file)
    assert risultato is None


def test_lista_file_bucket_vuoto():
    risposta = Mock()
    risposta.data.objects = []

    with patch("storage.object_storage.list_objects", return_value=risposta):
        risultato = lista_file()
    assert risultato == []

def test_lista_file_contenuto():
    oggetto1 = Mock()
    oggetto1.name = "documento.txt"

    oggetto2 = Mock()
    oggetto2.name = "foto.png"

    risposta = Mock()
    risposta.data.objects = [oggetto1, oggetto2]

    with patch("storage.object_storage.list_objects", return_value=risposta):
        risultato = lista_file()
    assert risultato == ["documento.txt", "foto.png"]

from storage import carica_file, lista_file, scarica_file


def test_scarica_file_successo(tmp_path):
    percorso_destinazione = tmp_path / "documento_scaricato.txt"

    risposta = Mock()
    risposta.status = 200
    risposta.data.content = b"Contenuto di prova"#b perchè il contenuto è binario

    with patch("storage.object_storage.get_object", return_value=risposta):
        risultato = scarica_file("documento.txt", percorso_destinazione)
    assert risultato == 200
    assert percorso_destinazione.read_bytes() == b"Contenuto di prova"


def test_scarica_file_non_trovato(tmp_path):
    percorso_destinazione = tmp_path / "documento.txt"

    errore = oci.exceptions.ServiceError(
        status=404,
        code="ObjectNotFound",
        headers={},
        message="Oggetto non trovato"
    )

    with patch("storage.object_storage.get_object", side_effect=errore):
        risultato = scarica_file("inesistente.txt", percorso_destinazione)
    assert risultato is None
    assert not percorso_destinazione.exists()


def test_scarica_file_destinazione_non_valida(tmp_path):
    percorso_destinazione = tmp_path / "cartella_inesistente" / "documento.txt"

    risposta = Mock()
    risposta.status = 200
    risposta.data.content = b"Contenuto di prova"

    with patch("storage.object_storage.get_object", return_value=risposta):
        risultato = scarica_file("documento.txt", percorso_destinazione)
    assert risultato is None