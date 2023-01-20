import datetime
import random

import faker
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

fake = faker.Faker()

departements = ["Informatique", "Mathématiques", "Physique"]

for i in range(300):
    diplome = fake.job()
    annee = random.randint(2000, 2021)
    departement = random.choice(departements)
    query = f"INSERT INTO Formation (diplome, annee, departement) VALUES ('{diplome}', {annee}, '{departement}')"
    cur.execute(query)

conn.commit()

# Insert fake data into the Equipe table
# Restart the sequence
cur.execute("ALTER SEQUENCE equipe_idequipe_seq RESTART WITH 1")

for i in range(300):
    nom = fake.word()
    slogan = fake.sentence()
    nb_points = random.randint(0, 1000)
    query = f"INSERT INTO Equipe (nom, slogan, nbPoints) VALUES ('{nom}', '{slogan}', {nb_points})"
    cur.execute(query)

conn.commit()

# Insert fake data into the Etudiant table
# Restart the sequence
cur.execute("ALTER SEQUENCE etudiant_idetudiant_seq RESTART WITH 1")
formations = list(range(1, 301))
equipes = list(range(1, 301))
for i in range(300):
    nom = fake.last_name()
    prenom = fake.first_name()
    adresse = fake.address()
    nb_points = random.randint(0, 1000)
    id_formation = random.choice(formations)
    id_equipe = random.choice(equipes)
    query = f"INSERT INTO Etudiant (nom, prenom, adresse, nbPoints, idFormation, idEquipe) VALUES ('{nom}', '{prenom}', '{adresse}', {nb_points}, {id_formation}, {id_equipe})"
    cur.execute(query)

conn.commit()

# Insert fake data into the Activite table
# Restart the sequence
cur.execute("ALTER SEQUENCE activite_idactivite_seq RESTART WITH 1")
now = datetime.datetime.now()
for i in range(300):
    nom = fake.sentence()
    date = now + datetime.timedelta(days=random.randint(-365, 365))
    lieu = fake.city()
    heures = random.randint(1, 6)
    minutes = random.randint(0, 59)
    duree = f"{heures}:{minutes}:00"
    descriptif = fake.paragraph()
    nb_points = random.randint(10, 500)
    nb_max = random.randint(10, 100)
    query = f"INSERT INTO Activite (nom, dateActivite, lieu, duree, descriptif, nbPoints, nbMax) VALUES ('{nom}', '{date}', '{lieu}', '{duree}', '{descriptif}', {nb_points}, {nb_max})"
    cur.execute(query)

conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
