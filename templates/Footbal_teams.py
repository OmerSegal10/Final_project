import MySQLdb

# Establish a connection to the database
db = MySQLdb.connect(host="localhost", user="root", passwd="Omer", db="sports_db")
cursor = db.cursor()

# Insert football teams
teams = [
    ("Maccabi Tel Aviv", "Football"),
    ("Hapoel Tel Aviv", "Football"),
    ("Maccabi Haifa", "Football"),
    ("Hapoel Be'er Sheva", "Football"),
    ("Bnei Sakhnin", "Football"),
    ("Beitar Jerusalem", "Football"),
    ("Ironi Kiryat Shmona", "Football"),
    ("Ashdod", "Football"),
    ("Hapoel Hadera", "Football"),
    ("Hapoel Kfar Saba", "Football"),
    ("Hapoel Haifa", "Football"),
    ("Maccabi Petah Tikva", "Football"),
    ("Maccabi Netanya", "Football"),
    ("Hapoel Ramat Gan", "Football")
]

# Insert each team into the teams table
for team in teams:
    cursor.execute('INSERT INTO teams (name, type) VALUES (%s, %s)', team)

# Commit changes and close the connection
db.commit()
cursor.close()
db.close()
