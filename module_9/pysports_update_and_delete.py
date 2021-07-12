import mysql.connector

db= mysql.connector.connect(
	host="localhost",
	user="root",
	password= "Luffy2209A@@",
	database= "pysports"
	)
#Update the database pysports in the player table by changing Harry Potter to The Chosen One Potter
mycursor = db.cursor()
sql = """UPDATE player SET team_id= "1", first_name= "Harry", last_name= "Potter" WHERE first_name= "The Chosen One"""

sql ="SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team\
 ON player.team_id = team.team_id"

mycursor.execute(sql)

#print the results of the update
info = mycursor.fetchall();
print("-----------Displaying Update Info-------------")
for team in info:
	print ("Player Id:  {}".format (team[1]))
	print ("First Name:  {}".format (team[2]))
	print ("Last Name:  {}".format (team[3]))
	print ("Team Name:  {}".format (team[4]))
	print()
	print ()

#Delete from the player table the update of The Chosen One Potter
mycursor = db.cursor()
sql = """DELETE FROM player WHERE team_id= "1", first_name= "The Chosen One", last_name= "Potter"""
sql ="SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team\
 ON player.team_id = team.team_id"

cursor.execute(sql)

#print the results of the deletion

info = mycursor.fetchall();
print("-----------Displaying Deletion Info-------------")
for team in info:
	print ("Player Id:  {}".format (team[1]))
	print ("First Name:  {}".format (team[2]))
	print ("Last Name:  {}".format (team[3]))
	print ("Team Name:  {}".format (team[4]))
	print()
	print ()

#Insert in data in the player table of James Potter
sql = """INSERT INTO player (player_id, first_name, last_name, team_id) VALUES (240, "James", "Potter", 1)"""

mycursor= db.cursor()
mycursor.execute(sql )

db.commit()

sql ="SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team\
 ON player.team_id = team.team_id"

info = mycursor.fetchall();
print("-----------Displaying Insert Info-------------")
for team in info:
	print ("Player Id:  {}".format (team[1]))
	print ("First Name:  {}".format (team[2]))
	print ("Last Name:  {}".format (team[3]))
	print ("Team Name:  {}".format (team[4]))
	print()
	print ()

