Explanation of the class diagram : 
The class diagram features the three layers of the application, the business layer where you can find the code of the classes, the Data Access Object (DAO) which stocks data in databasis and finally the control layer which is the terminal in our case.
The DAO class guarantees the permanent connection with the database, it stocks the players, characters, scenarios etc which have been created. 
The control layer calls the business layer which calls the DAO. 
In the business layer, there is, firstly, the User class defined by the name, the first name, the age, the username and the password. The Organiser and Player classes inherit of the User class as they are specific users. 
The Player Class displays a list of tables id, of half-days numbers and a notification attribute. There is also

Technology used : 
This application is coded in python. The entire code has been written by us, we have not used frameworks. The SQL language is also used to make all the requests to communicate with the database. This base is stocked on postgresql.
To obtain the list of the characters that the players can use, we use the D&D 5th API, its adress is http://www.dnd5eapi.co/ .
To collaborate and share our codes, we have used git hub. 