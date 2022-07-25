from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def nombre_funcion():
    return render_template("index.html")

@app.route('/algosucede')
def algosucede():
    return 'Oye, ¡Algo sucede -_- :O Q-Q!'

@app.route('/ahoralose/<string:frasex>/<int:num>')
def fase(frasex,num):
    return render_template("render.html", frasex=frasex,num=num)


@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    estudiantes_info = [
        {'name' : 'Michael', 'edad' : 35},
        {'name' : 'John', 'edad' : 30 },
        {'name' : 'Mark', 'edad' : 25},
        {'name' : 'KB', 'edad' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], estudiantes = estudiantes_info)



@app.errorhandler(404) #Error cuando la página no existe
def page_not_found(error):
    return 'This page does not exist', 404

if __name__=="__main__":
    app.run(debug=True)