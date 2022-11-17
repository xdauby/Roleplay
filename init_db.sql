DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

/*Création de la table organiser. */

CREATE TABLE organiser (
username TEXT PRIMARY KEY,
firstname TEXT,
lastname TEXT,
age INT DEFAULT NULL,
password TEXT
);

/*Création de la table player. */

CREATE TABLE player (
username TEXT PRIMARY KEY,
firstname TEXT,
lastname TEXT,
age INT DEFAULT NULL,
password TEXT
);

/*Création de la table scénario, on commence par la séquence.*/

CREATE SEQUENCE seq_id_scenario;

CREATE TABLE scenario (
id_scenario INT PRIMARY KEY DEFAULT nextval('seq_id_scenario'),
username TEXT REFERENCES player(username) ON DELETE CASCADE,
name TEXT,
description TEXT
);

/*Création de la table game.*/

CREATE SEQUENCE seq_id_game
MAXVALUE 80;

CREATE TABLE game (
id_game INT PRIMARY KEY DEFAULT nextval('seq_id_game'),
id_scenario INT REFERENCES scenario(id_scenario) ON DELETE SET NULL,
halfday INT,
active BOOL
);

/*Création de la table character.*/

CREATE SEQUENCE seq_id_char;

CREATE TABLE character (
id_char INT PRIMARY KEY DEFAULT nextval('seq_id_char'),
username TEXT REFERENCES player(username) ON DELETE CASCADE,
name TEXT,
level INT,
equipment TEXT,
race TEXT,
skill TEXT
);

/*Création de la table char_sub_table*/

CREATE TABLE char_reg_game (
id_game INT REFERENCES game(id_game),
id_char INT REFERENCES character(id_char) ON DELETE CASCADE,
CONSTRAINT pk_char_reg_table PRIMARY KEY(id_game, id_char)
);

/*Création de la table notif*/
CREATE SEQUENCE seq_id_notif;
CREATE TABLE notification (
id_notif INT PRIMARY KEY DEFAULT nextval('seq_id_notif'),
username TEXT REFERENCES player(username) ON DELETE CASCADE,
notif TEXT
);

/*Remplissage des valeurs (fictives ici)*/

INSERT INTO player VALUES
('coximor', 'Rémy', 'Dupont', 21,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('sephix','Jean','Dupuis',33,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('paya6','Jeanne','Durand',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('Jo89','Antoine','De Paepe',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('kkj3','Jean','Valjean',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('ghostminer','amine','ru',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('killer7','Jaques','Mesrine',15,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('lebloc','Denis','Motin',23,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('spiderman','Tim','Mossuz',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('batman77','Cedric','Chevaux',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('zoro','Cedric','Legrand',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('ziak','Moussa','Grand',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055'),
('ziakbis','George','Grand',19,'5cc55633769b725e714f9cdfc6c611e11e95bcb0f4f642ac922a373f0c91d055');

INSERT INTO organiser VALUES
('admin_orga2','Natasha','Duchar',39,'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'),
('admin_orga6','Jérémy','Deschamps',28,'8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918');

INSERT INTO scenario(username, name, description) VALUES
('sephix','A scary cave','Come with us explore a scary cave'),
('spiderman','The scary movie','Come with us play on a movie'),
('spiderman','Mister robot','Come with us hack computers'),
('batman77','Box fighting','Virtual box fights'),
('kkj3','No imagination','Virtual world using your imagination'),
('Jo89','A bad trip','Come get ayahuasca');


INSERT INTO character(username, name, level, equipment, race, skill) VALUES
('coximor', 'sorix', 62, 'amulet', 'bard','battleaxes'),
('sephix','battler',17,'backpack','wizard','breastplate'),
('coximor','cawa',3,'pony','rogue','longswords'),
('kkj3','cafe',3,'pony','rogue','longswords'),
('kkj3','rocketluri',5,'pony','rogue','longswords'),
('spiderman','spider',10,'pony','rogue','longswords'),
('ghostminer','miner1',12,'pony','rogue','longswords'),
('ghostminer','miner2',13,'pony','rogue','longswords'),
('ghostminer','miner3',14,'pony','rogue','longswords'),
('paya6','pinguin',5,'lyre','sorcerer','leather-armor'),
('zoro','bilibili',4,'lyre','sorcerer','leather-armor'),
('ziak','lacite',16,'lyre','sorcerer','leather-armor');

INSERT INTO notification(notif, username) VALUES
('You have been moved, check your tables !','coximor');

INSERT INTO game(id_scenario, halfday, active) VALUES
(1,1,TRUE),
(2,1,TRUE);

INSERT INTO char_reg_game(id_game, id_char) VALUES
(1,7),
(1,10),
(1,11),
(1,12),
(2,4);

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


INSERT INTO game(id_scenario, halfday, active) VALUES
(1,2,TRUE),
(2,2,TRUE);


INSERT INTO char_reg_game(id_game, id_char) VALUES
(22,10);

INSERT INTO game(halfday, active) VALUES
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,TRUE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE),
(2,FALSE);

INSERT INTO game(id_scenario, halfday, active) VALUES
(2,3,TRUE),
(6,3,TRUE);

INSERT INTO char_reg_game(id_game, id_char) VALUES
(41,1),
(41,9),
(41,10),
(42,4);

INSERT INTO game(halfday, active) VALUES
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,TRUE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE),
(3,FALSE);

INSERT INTO game(halfday, active) VALUES
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,TRUE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE),
(4,FALSE);


