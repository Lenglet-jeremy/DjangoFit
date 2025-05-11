
# Cloner le projet
git clone https://github.com/Lenglet-jeremy/DjangoFit.git

cd DjangoFitProject

# Créer et activer l'environnement virtuel
python3 -m venv ../DjangoFitEnv

source ../DjangoFitEnv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python3 manage.py migrate

# Lancer le serveur
python3 manage.py runserver

