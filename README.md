# Roleplay meeting application
***
# How to install :

Install python3.8 (__not supported after 3.8__)

__Install required package__

$ sudo apt-get install python3.8

$ pip install -r requirements.txt

Change connection informations in .env (you need psql)

Copy past init.db in your psql

__Then start__

$ python3.8 main.py

# Information :

If you want to test, for all players, the non-hashed password is : mdptest

If you want to test, for all organisers, the non-hashed password is : admin


# Example : 
If you want to participate to the meeting, you have to select "register as player". Then enter the information asked. The pseudo has to be unique, if someone has already taken it, the application will warn you. Once it is done, you are registered ! To reconnect you, you will have to select sign in and give your pseudo and your password.
If you want to play a game as a basic player, you will need a character. Choose the option "add character" and answer the information asked. As the pseudo of an user, the name of the character must be unique. It is the same procedure to add a scenario.
Finally, to be registered for a game, you have to join a table. Select the option and choose the id of the table you want to join. (you should have displayed the tables previously to know which one to choose) Then, say you want to join as a basic player with the character you just created. Remember, there must be a Game master on a table to play as a basic player. Now, you have finished you registration for a game, you can register for a game on another half-day if you like and with an other character you can create or as a game master if you add a scenario.


# Technology used : 
Python, SQL 
API used : http://www.dnd5eapi.co/
