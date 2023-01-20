import datetime
import random

import names
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="integrationday",
    user="postgres",
    password="admin"
)

# Create a cursor
cur = conn.cursor()

# Insert fake data into the Formation table
# Restart the sequence
cur.execute("ALTER SEQUENCE formation_idformation_seq RESTART WITH 1")
diplomes = ["Bachelor", "Master", "Doctorat", "Licence", "Ingénieur", "Commerce"]
departements = ["Informatique", "Mathématiques", "Physique", "Langues", "Français", "Mécanique", "Automatique", "Electronique"]

for i in range(100000):
    diplome = random.choice(diplomes)
    annee = random.randint(2000, 2021)
    departement = random.choice(departements)
    query = f"INSERT INTO Formation (diplome, annee, departement) VALUES ('{diplome}', {annee}, '{departement}')"
    cur.execute(query)
    if i % 10000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("Formation table filled !")

# Insert fake data into the Equipe table
# Restart the sequence
cur.execute("ALTER SEQUENCE equipe_idequipe_seq RESTART WITH 1")
slogans = ["Nous sommes les meilleurs !", "Plus forts, plus rapides, plus forts !", "Nous ne lâchons jamais !", "Realisons vos ambitions", "Decathlon, à fond la forme", "Mangez bougez.fr", "Les produits laitiers sont nos amis pour la vie", "Le sport est la vie", "Le sport est la santé", "Le sport est la vie !"]
for i in range(100000):
    nom = f"Equipe {i+1}"
    slogan = random.choice(slogans)
    nb_points = random.randint(0, 1000)
    query = f"INSERT INTO Equipe (nom, slogan, nbPoints) VALUES ('{nom}', '{slogan}', {nb_points})"
    cur.execute(query)
    if i % 10000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("Equipe table filled !")

# Insert fake data into the Etudiant table
# Restart the sequence
cur.execute("ALTER SEQUENCE etudiant_idetudiant_seq RESTART WITH 1")
formations = list(range(1, 100000))
equipes = list(range(1, 100000))
for i in range(1000000):
    nom = names.get_last_name()
    prenom = names.get_first_name()
    adresse = f"{random.randint(1, 1000)} rue de la Paix"
    nb_points = random.randint(0, 1000)
    id_formation = random.choice(formations)
    id_equipe = random.choice(equipes)
    query = f"INSERT INTO Etudiant (nom, prenom, adresse, nbPoints, idFormation, idEquipe) VALUES ('{nom}', '{prenom}', '{adresse}', {nb_points}, {id_formation}, {id_equipe})"
    cur.execute(query)
    if i % 100000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("Etudiant table filled !")

# Insert fake data into the Activite table
# Restart the sequence
cur.execute("ALTER SEQUENCE activite_idactivite_seq RESTART WITH 1")
now = datetime.datetime.now()
for i in range(100000):
    nom = f"Activité {i+1}"
    date = now + datetime.timedelta(days=random.randint(-365, 365))
    lieu = f"Lieu {i+1}"
    heures = random.randint(1, 6)
    minutes = random.randint(0, 59)
    duree = f"{heures}:{minutes}:00"
    descriptif = f"Descriptif de l activité {i+1}"
    nb_points = random.randint(10, 500)
    nb_max = random.randint(10, 100)
    query = f"INSERT INTO Activite (nom, dateActivite, lieu, duree, descriptif, nbPoints, nbMax) VALUES ('{nom}', '{date}', '{lieu}', '{duree}', '{descriptif}', {nb_points}, {nb_max})"
    cur.execute(query)
    if i % 10000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("Activite table filled !")

# Insert fake data into the InscriptionActivite table
activites = list(range(1, 100000))
etudiants = list(range(1, 1000000))
for i in range(100000):
    id_activite = random.choice(activites)
    id_etudiant = random.choice(etudiants)
    query = f"INSERT INTO InscriptionActivite (idActivite, idEtudiant) VALUES ({id_activite}, {id_etudiant})"
    cur.execute(query)
    if i % 10000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("InscriptionActivite table filled !")

# Insert fake data into the Challenge table
# Restart the sequence
cur.execute("ALTER SEQUENCE challenge_idchallenge_seq RESTART WITH 1")
for i in range(10000):
    nom = f"Challenge {i+1}"
    date = now + datetime.timedelta(days=random.randint(-365, 365))
    lieu = f"Lieu {i+1}"
    heures = random.randint(1, 6)
    minutes = random.randint(0, 59)
    duree = f"{heures}:{minutes}:00"
    descriptif = f"Descriptif du challenge {i+1}"
    nb_points = random.randint(500, 1000)
    nb_equipes = random.randint(5, 10)
    query = f"INSERT INTO Challenge (nom, dateChallenge, lieu, duree, descriptif, nbPoints, nbEquipes) VALUES ('{nom}', '{date}', '{lieu}', '{duree}', '{descriptif}', {nb_points}, {nb_equipes})"
    cur.execute(query)
    if i % 1000 == 0:
        print(f"{i} rows inserted")

conn.commit()
print("Challenge table filled !")

# Insert fake data into the InscriptionChallenge table
challenges = list(range(1, 10000))
for i in range(100000):
    id_challenge = random.choice(challenges)
    id_equipe = random.choice(equipes)
    query = f"INSERT INTO InscriptionChallenge (idChallenge, idEquipe) VALUES ({id_challenge}, {id_equipe})"
    cur.execute(query)
    if i % 10000 == 0:
        print(f"{i} rows inserted")

# Commit the transaction
conn.commit()
print("InscriptionChallenge table filled !")

# Close the cursor and the connection
cur.close()
conn.close()