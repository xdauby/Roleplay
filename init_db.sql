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

CREATE TABLE char_sub_game (
id_game INT REFERENCES game(id_game),
id_char INT REFERENCES character(id_char),
CONSTRAINT pk_char_sub_table PRIMARY KEY(id_game, id_char)
);


/*Remplissage des valeurs (fictives ici)*/

INSERT INTO player VALUES
('coximor', 'Rémy', 'Dupont', 21),
('sephix','Jean','Dupuis',33),
('paya6','Jeanne','Durand',19);

INSERT INTO organiser VALUES
('orga2','Natasha','Duchar',39),
('orga6','Jérémy','Deschamps',28);

INSERT INTO scenario(username, name, description) VALUES
('sephix','A scary cave','Come with us explore a scary cave');

INSERT INTO character(username, name, level, equipment, race, skill) VALUES
('coximor', 'sorix', '62', 'amulet', 'bard','battleaxes'),
('sephix','battler','17','backpack','wizard','breastplate'),
('coximor','cawa','3','pony','rogue','longswords'),
('paya6','pinguin','5','lyre','sorcerer','leather-armor');

INSERT INTO game(id_scenario, halfday, active) VALUES
(2,1,TRUE);

INSERT INTO char_sub_game VALUES
(3,5),
(3,8);