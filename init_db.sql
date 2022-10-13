DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

/*Création de la table organiser. */

CREATE TABLE organiser (
username TEXT PRIMARY KEY,
firstname TEXT,
lastname TEXT,
age INT DEFAULT NULL
);

/*Création de la table player. */

CREATE TABLE player (
username TEXT PRIMARY KEY,
firstname TEXT,
lastname TEXT,
age INT DEFAULT NULL
);

/*Création de la table scénario, on commence par la séquence.*/

CREATE SEQUENCE seq_id_scenario;

CREATE TABLE scenario (
id_scenario INT PRIMARY KEY DEFAULT nextval('seq_id_scenario'),
username TEXT REFERENCES player(username),
name TEXT,
description TEXT
);

/*Création de la table game.*/

CREATE SEQUENCE seq_id_game
MAXVALUE 80;

CREATE TABLE game (
id_game INT PRIMARY KEY DEFAULT nextval('seq_id_game'),
id_scenario INT REFERENCES scenario(id_scenario) DEFAULT NULL,
halfday INT,
active BOOL
);

/*Création de la table character.*/

CREATE SEQUENCE seq_id_char;

CREATE TABLE character (
id_char INT PRIMARY KEY DEFAULT nextval('seq_id_char'),
username TEXT REFERENCES player(username),
name TEXT,
level INT,
equipment TEXT,
equipment_desc TEXT DEFAULT NULL,
race TEXT,
race_desc TEXT DEFAULT NULL,
skill TEXT,
skill_desc TEXT DEFAULT NULL
);

/*Création de la table char_sub_table*/

CREATE TABLE char_reg_game (
id_game INT REFERENCES game(id_game),
id_char INT REFERENCES character(id_char),
CONSTRAINT pk_char_reg_table PRIMARY KEY(id_game, id_char)
);


/*Remplissage des valeurs (fictives ici)*/

INSERT INTO player VALUES
('coximor', 'Rémy', 'Dupont', 21),
('sephix','Jean','Dupuis',33),
('paya6','Jeanne','Durand',19),
('Jo89','antoine','de paepe',19),
('kkj3','antoine','caid',19);

INSERT INTO organiser VALUES
('orga2','Natasha','Duchar',39),
('orga6','Jérémy','Deschamps',28);

INSERT INTO scenario(username, name, description) VALUES
('sephix','A scary cave','Come with us explore a scary cave'),
('Jo89','A bad trip','Come get ayahuasca');


INSERT INTO character(username, name, level, equipment, race, skill) VALUES
('coximor', 'sorix', 62, 'amulet', 'bard','battleaxes'),
('sephix','battler',17,'backpack','wizard','breastplate'),
('coximor','cawa',3,'pony','rogue','longswords'),
('kkj3','cafe',3,'pony','rogue','longswords'),
('kkj3','rocketluri',5,'pony','rogue','longswords'),
('paya6','pinguin',5,'lyre','sorcerer','leather-armor');

INSERT INTO game(id_scenario, halfday, active) VALUES
(1,1,TRUE),
(2,1,TRUE),
(1,2,TRUE),
(2,2,TRUE);

INSERT INTO game(halfday, active) VALUES
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,TRUE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE),
(1,FALSE);


INSERT INTO char_reg_game VALUES
(1,5),
(1,6),
(4,2),
(4,5),
(4,6);

SELECT game.id_game FROM game
Left JOIN char_reg_game ON game.id_game=char_reg_game.id_game
right JOIN character ON character.id_char = char_reg_game.id_char
WHERE character.username = 'sephix';

#pour recup les id

SELECT * FROM player
LEFT JOIN character on character.username =  player.username
LEFT JOIN char_reg_game on char_reg_game.id_char =  character.id_char
LEFT JOIN game on game.id_game=char_reg_game.id_game
WHERE player.username = 'coximor';



SELECT DISTINCT game.id_game FROM character
LEFT JOIN char_reg_game on character.id_char =  char_reg_game.id_char
LEFT JOIN game on game.id_game = char_reg_game.id_game
WHERE character.username = 'coximor';


#pour les perso
SELECT * FROM game
inner JOIN char_reg_game on game.id_game = char_reg_game.id_game
inner JOIN character on character.id_char = char_reg_game.id_char
inner JOIN player on character.username = player.username
where game.id_game = 4 ;

#pour les games master 

SELECT * FROM game
inner JOIN scenario on game.id_scenario =  scenario.id_scenario
inner JOIN player on scenario.username = player.username
where game.id_game = 4 ;





recupere les id de talbles dans le joueur,
puis charger les tables avec la methode associer

simple car on aura 2 CAs : 1 pour le gamermaster, un pour le basicplayer


for 

SELECT * FROM game
LEFT JOIN char_reg_game on game.id_game = char_reg_game.id_game
inner JOIN character on character.id_char = char_reg_game.id_char
inner JOIN player on character.username = player.username
where game.id_game in (1,2,3,4) ;


SELECT * FROM game
inner JOIN scenario on scenario.id_scenario = game.id_scenario
inner JOIN player on scenario.username = player.username
where game.id_game in ;

