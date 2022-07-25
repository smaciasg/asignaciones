from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def ajedrez_basico():
    return render_template('index.html', filas=8,columnas=8,color1="aquamarine",color2="bisque")

@app.route('/<int:filas>')
def ajedrez_basico_lee_filas(filas):
    return render_template('index.html', filas=filas,columnas=8,color1="aquamarine",color2="bisque")

@app.route('/<int:filas>/<int:columnas>')
def ajedrez_basico_lee_filas_columnas(filas,columnas):
    return render_template('index.html', filas=filas,columnas=columnas,color1="aquamarine",color2="bisque")

@app.route('/<int:filas>/<int:columnas>/<string:color1>/<string:color2>')
def ajedrez_basico_lee_filas_columnas_colores(filas,columnas,color1,color2):
    return render_template('index.html', filas=filas,columnas=columnas,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)