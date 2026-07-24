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

## Deploy z GitLaba

Pipeline z pliku `.gitlab-ci.yml` wdraża zmiany po pushu do domyślnej gałęzi projektu. Na serwerze musi istnieć użytkownik `deploy`, katalog `/var/www/flask-app`, środowisko `/var/www/flask-app/.venv` oraz usługa systemd `flask-app`. Użytkownik `deploy` musi mieć uprawnienia `sudo` do restartowania i sprawdzania tej usługi.

W GitLabie, w `Settings → CI/CD → Variables`, dodaj:

- `DEPLOY_HOST` — adres serwera,
- `DEPLOY_USER` — opcjonalnie, domyślnie `deploy`,
- `SSH_PRIVATE_KEY` — prywatny klucz SSH, jako zmienna typu **File**, oznaczona jako **Protected** jeśli domyślna gałąź jest protected,
- `SSH_KNOWN_HOSTS` — wynik `ssh-keyscan -H ADRES_SERWERA`, również jako zmienna typu **File**.

Klucz publiczny dodaj do `/home/deploy/.ssh/authorized_keys` na serwerze. Zmienna `SSH_KNOWN_HOSTS` pozwala pipeline’owi weryfikować tożsamość serwera bez wyłączania sprawdzania host key.

## Endpointy

- `GET /` — zwraca `Hello, World!` oraz potwierdzenie połączenia z MySQL.
- `GET /health` — prosty endpoint sprawdzający, czy aplikacja działa.

## Udział w projekcie

Zasady zgłaszania zmian opisano w [CONTRIBUTING.md](CONTRIBUTING.md). Obowiązuje również [Code of Conduct](CODE_OF_CONDUCT.md).

## Bezpieczeństwo

Informacje o zgłaszaniu luk bezpieczeństwa znajdują się w [SECURITY.md](SECURITY.md).

## Licencja

Projekt jest dostępny na licencji [MIT](LICENSE).
