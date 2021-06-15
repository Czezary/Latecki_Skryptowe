

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about")
def about_me():
    dane = {'tytul':'o mnie','tresc':'yo soy me nombre es czaro'}
    return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])
@app.route("/info")
def information():
    posty = [{
    'author': {'username': 'ryszard'},
    'body': 'fsafsafeeeewwwwwwwwsdadsdsafsafsafsafsa'
    },
    {
    'author': {'username': 'ryszard2'},
    'body': 'no spam plis'
    },
     {
    'author': {'username': 'ryszard3'},
    'body': 'yes no spam'
    }
     ]
    dane = {'tytul':'informacje','tresc':'forum 4chan'}
    return render_template('informacje.html', tytul=dane['tytul'], tresc=dane['tresc'],posty=posty)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
