import mysql.connector

db= mysql.connector.connect(
	host="localhost",
	user="root",
	password= "Luffy2209A@@",
	database= "pysports"
	)

cursor = db.cursor()

sql ="SELECT\
 player_id, first_name, last_name, team_name \
 FROM player\
 INNER JOIN team\
 ON player.team_id = team.team_id"

cursor.execute(sql)

result = cursor.fetchall();
print(result)

