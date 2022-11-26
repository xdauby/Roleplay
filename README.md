# Roleplay meeting application
***
# How to install :

install python3.8 (not supported after 3.8)
install required package

$ sudo apt-get install python3.8
$ pip install -r requirements.txt

change connection informations in .env (you need psql)
copy past init.db in your psql

Then start
$ python3.8 main.py

# Information :
If you want to test, for all players, the non-hashed password is : mdptest
If you want to test, for all organisers, the non-hashed password is : admin

# Explanation of the class diagram : 
The class diagram features the three layers of the application, the business layer where you can find the code of the classes, the Data Access Object (DAO) which stocks data in databasis and finally the controller layer which is the terminal in our case. The DAO class guarantees the permanent connection with the database, it stocks the players, characters, scenarios etc which have been created. 
The controller layer calls the business layer which calls the DAO.  In the business layer, there is, firstly, the User class defined by the name, the first name, the age, the username and the password. The Organiser and Player classes inherit of the User class as they are specific users. 
The Player Class displays a list of tables id, of half-days numbers and a notification attribute. This attribute is neal by default and is a string object sent to the player when the organizer has made an action on a table where he was registered (moved, deleted, banned...).
There is also an attribute that corresponds to his profile, in fact the GameMaster and BasicPlayer classes can be seen as the profils of players. 
A player has also a save method : it does not allow him to save all his attributes but only the followings : name, first name, age, username.
The delete method deletes a player in database. The player is, therefore, deleted from all the table where he is registered. His scenarios and characters will be saved thaks to other methods. The delete method is also a way for the organiser to ban players.
The BasicPlayer and GameMaster classes are linked with Player thanks to a composition relation : they cannot exist without the player. It is the same type of link between BasicPlayer and Character because a player cannot play without a character and his characterds are deleted when the player is deleted.
A player can create 3 characters maximum and a character is unique, it is linked to only one player. A character has a unique id, a name and some features such as the level, the race and the class. These two last attributes have a description for each that is obtainable in a dict type by the get_description() method.
The Character class communicates with a webservice (ServiceDG class) where are taken the character's attributes. When a player wants to create a character, he has two choices : directly write the class and the race of the character and then the Webservice will find the corresponding descriptions or choose among a list available in the Webservice.
The GameMaster exists thanks to the scenarios he creates, thus, there is a composition link between theses two classes. At the beginning, his list of scenarios is empty but he can add and deletes scenarios with a limit of 2 scenaarios in the list. A scenario has a name, an id and a description. Scenarios are automatically uploaded in databases beacause the Game Master class calls the class GameMasterDAO.
Contrarly to the previous examples, when we delete a table, the players are not deleted : it is not a composition but an agregation relation. The table can contain from 0 to 5 players including 1 GameMaster and 4 BasicPlayer. The Table has, thereby, an attribute gamemaster and an attribute basciplayer which is a list of maximum 4 basic players.
Players have a list of tables id as an attribute to avoid redundancy.
The BasicPlayer inherits of the Player class and has a composition link with the class Character. Thus, the character has as attributes the id of his basic player and his pseudo.
It is the same type of link between GameMaster and Scenario, if the game master is deleted, the scenarios are deleted too. The GameMaster has a list of scenarios with a lenght between 0 and 2. The scenario has, as attributes, the id and the pseudo of the GameMaster who created it.
The load methods are static methods directly calling methods from DAO classes. Thus, we test them in the DAO classes.
The ServiceDG class is a webservice containing the features of the characters that the players can access when he wants to create a character. It has, in attributes, the access path to the webservice and to the different features (equipment_root, race_root, skill_root). The method get_features givves a sight of the characteristics of characters among which the player can chhose. get descriptions gives the description of a particular feature asked by the player. 
The controller layer calls the business layer. More precisely, the Session class which is a singleton uses the classes of the business layer.The goal is to stock temporary attributes to avoid stocking all the instances created in the Views.
Some views are shared by all the classes and other views specific to the organisers such as BanView for example.
The DAO stocks the objects created in database, without it, every thing would disappear after the closure of the programme. The DAO of player includes two DAO : GameMaster and BasicPlayerDao which are not on the diagram to make it easier to read. 
Each DAo is specialized, there is a DAo for each type of object. On top of that, some DAO use other DAO usch as PlayerDao using ScenarioDao and CharacterDao because loading a plyer implies loading his characters and scenarios. Everu classes of DAO type use the singleton DBConnection

# What can be achieved with the application :
This application is designed to help organising a role play meeting. It deals with the registration of the players and game masters for a game giving also to organisers flexible possibilities to organise their meeting.
This meeting takes place during a week-end, with 4 4-hour sessions of game, one during each half-day. 
There are two types of users : the players and the organisers. These lasts can deal with the table : they can ban players, remove them from a table, add tables but has also a hand on the characters and scenarios created by players. 
A game can welcome 5 players, among them, there must be a game player to bring his scenario and make the game happen? Then, 4 basic players can join and at least two. Thus, these are the two types of players and a player can choose between both for each half-day.
Initially, 10 tables are available et ready to welcome players for each half-day. The organisers can add other tables if necessary but it cannot be more than 20.

Firstly, an user has a menu offering to either sign in as a player or an organiser or to register as a player. The organiser does not need to register because he is automatically registered and has a username and a password attributed automatically. It is not possible to sign-in if the player has never registered before.
When the player is connected, he has several options. He can, for example, create a charcater or a scenario, he must enter the name and some features of what he is creating. He must of course, enter appropriate things such as a number for the level. If it is not the case, an error message occurs. 
The player can display his characters and scenarios with the option in the menu. Thanks to this, he can see their characteristics and their id.
This id is useful to register at a table because this what is asked to choose the character or the scenario. To register at a table, it is necessary to choose a compatible table with what type of player chosen for the game. For example, to register on a table as a game master, the table must be empty. It is the opposite to register as basic player, there must already be a game master on the table. The table must also not be full. If there is on this problem, the application will say it to the user and not make the action asked. 
To be sure to choose a good table, there is an option to diplay the tables and see which ones are available and hae scenarios that are interesting etc. 
There is also the possibility to display only the tables where the user has registered. The player can also cancel his registration to a table. Finally, he can disconnect.
The organiser has a menu with a similar but different range of possibilities. 
When the organiser displays the table, he sees all the tables : 80, 20 per half-day. Some of them are desactivate and he can activate them when he wants. The player only sees the activated tables when he displays the tables. 
An organiser can also add a table, it activates a table which was inactive. 
He can delete a table : all the players are removed from the table and the table is desactivated. 
There is also the possibility to remove a particular player from a table if his character does not correspond well to the scenario for example. Then, the organiser can add him to another table. 
The organiser can also ban a player who will consequently be removed from all the tables.
When a player is removed from a table or added to another one, he will receive a notification the next time he will log-in.  
All these possibilities allow the player to participate to the meeting with the characters or scenarios they want on a table they have chosen and allow the organiser to deal with tables to optimize the repartition of the players on the tables for example. 

# Example : 
If you want to participate to the meeting, you have to select "register as player". Then enter the information asked. The pseudo has to be unique, if someone has already taken it, the application will warn you. Once it is done, you are registered ! To reconnect you, you will have to select sign in and give your pseudo and your password.
If you want to play a game as a basic player, you will need a character. Choose the option "add character" and answer the information asked. As the pseudo of an user, the name of the character must be unique. It is the same procedure to add a scenario.
Finally, to be registered for a game, you have to join a table. Select the option and choose the id of the table you want to join. (you should have displayed the tables previously to know which one to choose) Then, say you want to join as a basic player with the character you just created. Remember, there must be a Game master on a table to play as a basic player. Now, you have finished you registration for a game, you can register for a game on another half-day if you like and with an other character you can create or as a game master if you add a scenario.


# Technology used : 
This application is coded in python. The entire code has been written by us. The SQL language is also used to make all the requests to communicate with the database. This base is stocked on postgresql.
To obtain the list of the characters that the players can use, we use the D&D 5th API, its adress is http://www.dnd5eapi.co/ .
To collaborate and share our codes, we have used git hub. 