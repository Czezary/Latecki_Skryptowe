import json
import re
from urllib import response

from flask import Flask,Response,redirect,url_for,request,session,abort,render_template
from flask_login import LoginManager,UserMixin,login_required,login_user,logout_user
import sqlite3 as sql
app = Flask(__name__)

app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_key'
)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "maniac"
    
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name,self.password)


users = [User(id) for id in range(1, 10)]

@app.route("/")
@login_required 
def main():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    title = 'Log in'
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == username + "maniac":
            id = username.split('user')[1]
            user = User(id)
            login_user(user)
            return redirect(url_for("main"))
        else:
            return abort(401)
    else:
        return render_template('logon.html', title=title)
    
@app.errorhandler(401)
def page_not_found(e):
    title="Something went wrong"
    err = "401"
    return render_template('err.html', title=title, err=err)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    tytul="LoggedOut"
    return render_template('logout.html', tytul=tytul)



@login_manager.user_loader
def load_user(userid):
    return User(userid)


@app.route("/register")
def new_pracownik():
    dane={'title':'Add tank'}
    return render_template('register.html',title=dane['title'])

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    dane={'title':'Result'}
    if request.method == 'POST':
        try:
            OwnerName = request.form['OwnerName']
            TankName = request.form['TankModel']
            TankModel = request.form['TankModel']
            TankYear = request.form['TankYear']
            TankNationality=request.form['TankNationality']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Tanklist (OwnerName,TankName,TankModel,TankYear,TankNationality) VALUES(?,?,?,?,?)",(OwnerName,TankName,TankModel,TankYear,TankNationality) )
                con.commit()
                msg = "Record Saved"
        except:
            con.rollback()
            msg = "ERROR, could not add record"
        
        finally:
            return render_template("result.html",title=dane['title'],msg = msg)
            con.close()


@app.route('/registered')
def list():
    dane={'title':'Tank list'}
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM Tanklist ORDER BY TankYear ASC')
    records = cur.fetchall();
    return render_template("registered.html",title=dane['title'] ,records = records)

if __name__ == "__main__":
    app.run()
