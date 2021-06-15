import sqlite3

conn = sqlite3.connect('database.db')
print("Database online")

conn.execute('CREATE TABLE pracownicy (imie TEXT,nazwisko TEXT, nr_pracownika TEXT, adres TEXT)')
print("Table created")

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nr_pracownika,adres) VALUES(?,?,?,?)",('ryszard', 'ryszardowicz','1','ryszardowska'))
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nr_pracownika,adres) VALUES(?,?,?,?)",('zbyniu', 'kowalksi','2','jakastam 22'))
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nr_pracownika,adres) VALUES(?,?,?,?)",('jendrzej', 'armowicz','3','jakastam 47'))
cur.execute("INSERT INTO pracownicy (imie,nazwisko,nr_pracownika,adres) VALUES(?,?,?,?)",('andzej', 'bobo','4','grozna 2'))

cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
conn.commit()
print(cur.fetchall())
conn.close()
