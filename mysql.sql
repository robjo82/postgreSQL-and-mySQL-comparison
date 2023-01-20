CREATE TABLE Formation (
    idFormation SERIAL PRIMARY KEY NOT NULL,
    diplome VARCHAR(50),
    annee INTEGER,
    departement VARCHAR(50)
);

create table Equipe (
    idEquipe serial primary key not null,
    nom varchar(50),
    slogan text,
    nbPoints Integer
);

create table Etudiant (
    idEtudiant serial primary key not null,
    nom varchar(30),
    prenom varchar(30),
    adresse text,
    nbPoints integer,
    idFormation serial not null,
    idEquipe serial not null,
    foreign key (idFormation) references formation(idFormation),
    foreign key (idEquipe) references equipe(idEquipe)
);

create table Activite (
    idActivite serial primary key not null,
    nom varchar(50),
    dateActivite date,
    lieu text,
    duree time,
    descriptif text,
    nbPoints integer,
    nbMax integer
);

create table InscriptionActivite(
    idActivite serial not null,
    idEtudiant serial not null,
    foreign key (idActivite) references Activite(idActivite),
    foreign key (idEtudiant) references Etudiant(idEtudiant)
);

create table Challenge(
    idChallenge serial primary key not null,
    nom varchar(50),
    dateChallenge date,
    lieu text,
    duree time,
    descriptif text,
    nbPoints integer,
    nbEquipes integer
);

CREATE TABLE InscriptionChallenge (
    idChallenge SERIAL NOT NULL,
    idEquipe SERIAL NOT NULL,
    FOREIGN KEY (idChallenge)
        REFERENCES Challenge (idChallenge),
    FOREIGN KEY (idEquipe)
        REFERENCES Equipe (idEquipe)
);