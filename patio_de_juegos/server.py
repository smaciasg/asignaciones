from click import style
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def pagina_inicio():
    return render_template("niveldos.html",cantidad=3,color="aquamarine")

@app.route('/play/<int:x>')
def crear_cadricula(x):
    return render_template("niveldos.html",cantidad=x,color="aquamarine")

@app.route('/play/<int:x>/<string:color>')
def crear_cadricula_color(x,color):
    return render_template("niveldos.html",cantidad=x,color=color)

if __name__=="__main__":
    app.run(debug=True)