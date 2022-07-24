from flask import Flask
app = Flask(__name__)

#EJERCICIO 1: Localhost:5000/: haz que diga "¡Hola Mundo!"
@app.route('/')
def saludar():
    return "¡Hola mundo!"

#EJERCICIO 2: Localhost:5000/dojo: haz que diga "¡Dojo!"
@app.route('/dojo')
def dojo():
    return "¡Dojo!"

#EJERCICIO 3: Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos:
# localhost:5000/say/flask: haz que diga "¡Hola, Flask!"
# localhost:5000/say/ Michael: haz que diga "¡Hola, Michael!"
# localhost:5000/say/john: haz que diga "¡Hola, John!"
@app.route('/say/<string:valor>')
def saludo_valor(valor):
    return f"¡Hola, {valor}!"

#EJERCICIO 4: Crea un patrón y una función de URL que puedan manejar los siguientes ejemplos (PISTA: int() puede ser útil Por ejemplo, int("35") devuelve 35):
# localhost:5000/repeat/35/hello: haz que diga "hola" 35 veces
# localhost:5000/repeat/80/bye: haz que diga "adiós" 80 veces
# localhost:5000/repeat/99/dogs: haz que diga "perros" 99 veces
@app.route('/repeat/<string:expresion>/<int:repeticion>')
def repeat(expresion,repeticion):
    tex = ""
    for i in range(0,repeticion):
        tex += f"<p>{expresion}</p>"
    return tex

if __name__=="__main__":
    app.run(debug=True)