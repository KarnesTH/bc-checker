# BC-Checker (Baustoff-Checker)

Ein Web-Dashboard zur Aggregation und zum Vergleich von Baustoffpreisen verschiedener Anbieter.

## Features

- Login- & Benutzerverwaltung
- Baustoff-Preisvergleich in Echtzeit
- Automatisches Crawling von Baustoffdaten
- Admin-Panel zur Datenverwaltung
- RESTful API
- Responsive UI

## Technologie-Stack

- **Backend**: Python/Flask
- **Datenbank**: SQLAlchemy
- **Frontend**: React(TypeScript)
- **Deployment**: Docker

## Installation

1. Repository klonen:
```bash
git clone https://github.com/KarnesTH/bc-checker.git
cd bc-checker
```

2. Virtuelle Umgebung erstellen:
```bash
cd backend
python -m venv env
source env/bin/activate  # Unter Windows: env\Scripts\activate
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

4. Docker Container starten:
```bash
docker-compose up -d
```

## Lizenz

MIT License - siehe [LICENSE](LICENSE)
