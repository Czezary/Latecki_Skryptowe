from flask import Flask, render_template,request,Flask,Response,redirect,url_for,request,session,abort,render_template
import sqlite3 as sql

from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import sqlite3 as sql

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='sekretny_klucz'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)



users = [User(id) for id in range(1, 10)]


@app.route("/")
@login_required
def main():
    return render_template('baza.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    tytul = 'Logowanie'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "_secret":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("main"))
        else:
            return abort(401)
    else:
        return render_template('formularz.html', tytul=tytul)


@app.errorhandler(401)
def page_not_found(e):
    tytul = "Cos sie zepsulo i nie bylo mnie slychac"
    blad = "401"
    return render_template('err.html', tytul=tytul, blad=blad)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    tytul = "Log out"
    return render_template('logout.html', tytul=tytul)


@login_manager.user_loader
def load_user(userid):
    return User(userid)


app = Flask(__name__)
@app.route("/")
def main():
    return  render_template('baza.html')

@app.route("/dodaj")
def new_pracownik():
    dane={'tytul':'Dodaj pracownika'}
    return render_template('dodajpracownika.html',tytul=dane['tytul'])

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    dane={'tytul':'Rezultat'}
    if request.method == 'POST':
        try:
            imie = request.form['imie']
            nazwisko = request.form['nazwisko']
            nr_pracownika = request.form['nr_pracownika']
            adres = request.form['adres']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pracownicy (imie,nazwisko,nr_pracownika,adres) VALUES(?,?,?,?)",(imie,nazwisko,nr_pracownika,adres) )
                
                con.commit()
                msg = "Record saved"
        except:
            con.rollback()
            msg = "Err "
        
        finally:
            return render_template("wynik.html",tytul=dane['tytul'],msg = msg)
            con.close()


@app.route('/lista')
def list():
    dane={'tytul':'Lista pracowników'}
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
    rekordy = cur.fetchall();
    return render_template("lista.html",tytul=dane['tytul'] ,rekordy = rekordy)

if __name__ == "__main__":
    app.run()

