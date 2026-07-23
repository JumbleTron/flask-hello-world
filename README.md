# Hello World — Flask + MySQL

Prosta aplikacja Flask, która na endpointcie `/` zwraca komunikat i wykonuje testowe zapytanie do MySQL.

## Uruchomienie

1. Uruchom bazę danych:

   ```bash
   docker compose up -d mysql
   ```

2. Utwórz środowisko wirtualne i zainstaluj zależności:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Skopiuj konfigurację:

   ```bash
   cp .env.example .env
   ```

4. Uruchom aplikację:

   ```bash
   python app.py
   ```

Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000.

## Endpointy

- `GET /` — zwraca `Hello, World!` oraz potwierdzenie połączenia z MySQL.
- `GET /health` — prosty endpoint sprawdzający, czy aplikacja działa.

## Udział w projekcie

Zasady zgłaszania zmian opisano w [CONTRIBUTING.md](CONTRIBUTING.md). Obowiązuje również [Code of Conduct](CODE_OF_CONDUCT.md).

## Bezpieczeństwo

Informacje o zgłaszaniu luk bezpieczeństwa znajdują się w [SECURITY.md](SECURITY.md).

## Licencja

Projekt jest dostępny na licencji [MIT](LICENSE).
