from distutils.log import debug
from flask import Flask
app = Flask(__name__)

@app.route('/')
def nombre_funcion():
    return '¡Hola Sebas!'

@app.route('/algosucede')
def algosucede():
    return 'Oye, ¡Algo sucede -_- :O Q-Q!'

@app.route('/ahoralose/<string:frasex>/<int:num>')
def fase(frasex,num):
    return f"Ahora lo sé, debo cambiar mi camino {num*frasex}"

if __name__=="__main__":
    app.run(debug=True)