from flask import Flask,Response,redirect,url_for,request,session,abort,render_template
from flask_login import LoginManager,UserMixin,login_required,login_user,logout_user
import sqlite3 as sql
app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'wpyte'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "wpyte"
    
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name,self.password)


users = [User(id) for id in range(1, 2)]

@app.route("/")
@login_required
def main():
    return render_template('baza.html')

@app.route("/about")
@login_required
def omnie():
    tytul = 'O mnie'
    return render_template('omnie.html', tytul=tytul)

@app.route("/login", methods=["GET", "POST"])
def login():
    tytul = 'Login'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "wpyte":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("main"))
        else:
            return abort(401)
    else:
        return render_template('form.html', tytul=tytul)
    
@app.errorhandler(401)
def page_not_found(e):
    tytul="cos sie zepsulo"
    blad = "401"
    return render_template('err.html', tytul=tytul, blad=blad)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    tytul="Log out"
    return render_template('logout.html', tytul=tytul)


@login_manager.user_loader
def load_user(userid):
    return User(userid)


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
            nrpracownika = request.form['nrpracownika']
            adres = request.form['adres']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pracownicy (imie,nazwisko,nrpracownika,adres) VALUES(?,?,?,?)",(imie,nazwisko,nrpracownika,adres) )
                
                con.commit()
                msg = "Record saved"
        except:
            con.rollback()
            msg = "adding error"
        
        finally:
            return render_template("wynik.html",tytul=dane['tytul'],msg = msg)
            con.close()


@app.route('/lista')
def list():
    dane={'tytul':'Lista pracownikow'}
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM pracownicy ORDER BY nazwisko')
    rekordy = cur.fetchall();
    return render_template("lista.html",tytul=dane['tytul'] ,rekordy = rekordy)

if __name__ == "__main__":
    app.run()
