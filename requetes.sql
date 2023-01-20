SELECT * from etudiant ;
select idetudiant from etudiant ;
select nom from etudiant ;
select nom from equipe ;
select adresse from etudiant ;
select datechallenge from challenge ;
select duree from challenge;

select nom, prenom from etudiant where nbpoints = 10 ;
select nom, prenom from etudiant where idetudiant = 25;
select nom, prenom from etudiant where nbpoints > 10 ;
select nom, prenom from etudiant where nbpoints > 10 and nbpoints < 20 ;
select nom, prenom from etudiant where nbpoints < 10 or nbpoints > 20 ;
select nom, prenom from etudiant where prenom = 'Martin' ;
select nom, prenom from etudiant where adresse = 'Valenciennes';
select nom, prenom from etudiant where (nbpoints = 10 and adresse = 'Valenciennes') ;
select nom from challenge where datechallenge > '10/02/2022' ;


select * from etudiant, equipe;
select * from etudiant, equipe, formation;
select etudiant.nom, etudiant.prenom from etudiant, equipe where etudiant.idequipe = equipe.idequipe ;
select etudiant.nom, etudiant.prenom
    from etudiant, equipe
    where (etudiant.idequipe = equipe.idequipe and equipe.nom = 'Equipe1');
select etudiant.nom, etudiant.prenom
    from etudiant, equipe, formation
    where   etudiant.idequipe = equipe.idequipe and
            etudiant.idformation = formation.idformation and
            equipe.nom = 'Equipe1' and formation.annee > 2020 ;

select etudiant.nom, etudiant.prenom
    from etudiant, equipe, formation
    where   etudiant.idequipe = equipe.idequipe and
            etudiant.idformation = formation.idformation and
            equipe.nom = 'Equipe1' and formation.annee > 2020
    order by etudiant.nbpoints desc ;
select etudiant.nom, etudiant.prenom
    from etudiant, equipe, formation
    where   etudiant.idequipe = equipe.idequipe and
            etudiant.idformation = formation.idformation and
            equipe.nom = 'Equipe1' and formation.annee > 2020
    order by etudiant.nbpoints ;

select etudiant.nom, etudiant.prenom
    from etudiant, equipe, formation
    where   etudiant.idequipe = equipe.idequipe and
            etudiant.idformation = formation.idformation and
            equipe.nom = 'Equipe1' and formation.annee > 2020 and
            etudiant.idetudiant < 50
    order by etudiant.nbpoints ;

select etudiant.nom, etudiant.prenom
    from etudiant, equipe, formation
    where   etudiant.idequipe = equipe.idequipe and
            etudiant.idformation = formation.idformation and
    having
