# SPOTILIKE
Par Chloé Chiarlini et Astrid Pierron

## Description
**Spotilike** est une application web semblable à Spotify, permettant de gérer des albums musicaux grâce à une API REST.

## Structure du projet
- **Backend** : Python et Django pour l'API REST.
- **Frontend** : React pour l'interface utilisateur.

## Prérequis
- **Python**
- **Django**
- **Node.js**

## Installation

### 1. Clonez le dépôt

### 2. Créez et activez un environnement virtuel

#### Sous Windows :
```
python -m venv django-venv
.\django-venv\Scripts\activate
```

#### Sous macOS/Linux :
```
python3 -m venv django-venv
source django-venv/bin/activate
```

### 3. Installez les dépendances backend
```
pip install -r requirements.txt
```

### 4. Configurez la base de données
Appliquez les migrations pour initialiser la base de données :
```
python manage.py migrate
```

### 5. Chargez les données initiales
Pour pré-remplir la base de données avec des données, exécutez le script `db.py` :
```
python db.py
```

### 6. Installez les dépendances frontend
Accédez au dossier du frontend React :
```
cd spotilike-app
npm install
```

### 7. Lancez les serveurs backend et frontend

#### Backend (Django) :
Démarrez le serveur de développement Django :
```
python manage.py runserver
```

Accédez à l'application backend via l'adresse suivante : [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### Frontend (React) :
Dans le dossier `spotilike-app/`, démarrez le serveur de développement React :
```
npm start
```

Accédez à l'application frontend via l'adresse suivante : [http://localhost:3000](http://localhost:3000).
