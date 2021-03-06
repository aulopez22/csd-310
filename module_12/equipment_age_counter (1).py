import mysql.connector

#connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "rBillie-0928t",
    database= "outlandadventures"
)

#create a cursor
cursor = db.cursor()

#Count how much equipment is older than five years old
cursor.execute('SELECT COUNT(*) FROM supplies WHERE CAST(date_added AS DATE) < NOW() - interval 5 year;')
info = cursor.fetchall()

print()
print()
print("-- DISPLAYING SUPPLIES RECORDS --")
print(f"Equipment older than 5 years: {info[0][0]}")


#Count how much equipment is newer than five years old
cursor.execute('SELECT COUNT(*) FROM supplies WHERE CAST(date_added AS DATE) >= NOW() - interval 5 year;')
infotwo = cursor.fetchall()
print(f"Equipment 5 years old or newer: {infotwo[0][0]}")
print()
print()

#close the database
db.close()