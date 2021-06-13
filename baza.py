import sqlite3

conn = sqlite3.connect('database.db')
print("Baza otwarta")

conn.execute('CREATE TABLE Tanklist (OwnerName TEXT,TankName TEXT,TankModel TEXT, TankYear TEXT,TankNationality TEXT)')
print("Table created")

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("INSERT INTO Tanklist (OwnerName,TankName,TankModel,TankYear,TankNationality) VALUES(?,?,?,?,?)",('sławek', 'Panther','A','1942','Germany'))
cur.execute("INSERT INTO Tanklist (OwnerName,TankName,TankModel,TankYear,TankNationality) VALUES(?,?,?,?,?)",('ryszard', 'Tiger','H1','1942','Germany'))
cur.execute("INSERT INTO Tanklist (OwnerName,TankName,TankModel,TankYear,TankNationality) VALUES(?,?,?,?,?)",('leszek', 'Sherman','VC','1944','United Kingdom'))
cur.execute("INSERT INTO Tanklist (OwnerName,TankName,TankModel,TankYear,TankNationality) VALUES(?,?,?,?,?)",('andzej', 'T-34-85','A','1944','USSR'))


cur.execute('SELECT * FROM Tanklist ORDER BY TankYear ASC')
conn.commit()
print(cur.fetchall())
conn.close()
