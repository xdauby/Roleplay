Explanation of the class diagram : 
The class diagram features the three layers of the application, the business layer where you can find the code of the classes, the Data Access Object (DAO) which stocks data in databasis and finally the controller layer which is the terminal in our case.
The DAO class guarantees the permanent connection with the database, it stocks the players, characters, scenarios etc which have been created. 
The controller layer calls the business layer which calls the DAO. 

In the business layer, there is, firstly, the User class defined by the name, the first name, the age, the username and the password. The Organiser and Player classes inherit of the User class as they are specific users. 
The Player Class displays a list of tables id, of half-days numbers and a notification attribute. This attribute is neal by default and is a string object sent to the player when the organizer has made an action on a table where he was registered (moved, deleted, banned...).
There is also an attribute that corresponds to his profile, in fact the GameMaster and BasicPlayer classes can be seen as the profils of players. 
A player has also a save method : it does not allow him to save all his attributes but only the followings : name, first name, age, username.
The delete method deletes a player in database. The player is, therefore, deleted from all the table where he is registered. His scenarios and characters will be saved thaks to other methods. The delete method is also a way for the organiser to ban players.
The BasicPlayer and GameMaster classes are linked with Player thanks to a composition relation : they cannot exist without the player. It the same type of link between BasicPlayer and Character because a player cannot play without a character and his characterds are deleted when the player is deleted.
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

What can be achieved with the application :


Technology used : 
This application is coded in python. The entire code has been written by us, we have not used frameworks. The SQL language is also used to make all the requests to communicate with the database. This base is stocked on postgresql.
To obtain the list of the characters that the players can use, we use the D&D 5th API, its adress is http://www.dnd5eapi.co/ .
To collaborate and share our codes, we have used git hub. 