# Python Cloud Storage

Applicazione Python per gestire file su **Oracle Cloud Infrastructure (OCI) Object Storage**.

## Funzionalità

- Caricamento di file nel bucket.
- Visualizzazione dei file presenti nel bucket.
- Download dei file.

## Tecnologie utilizzate

- Python
- Oracle Cloud Infrastructure (OCI) SDK
- Pytest

## Installazione

Installare le dipendenze:

```bash
pip install -r requirements.txt
```

## Utilizzo

Eseguire gli script dalla cartella del progetto:

```bash
python carica_file.py
python lista_file.py
python scarica_file.py
```

## Test

Per eseguire i test automatici:

```bash
python -m pytest -v
```
