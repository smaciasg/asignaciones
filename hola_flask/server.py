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

@app.errorhandler(404) #Error cuando la página no existe
def page_not_found(error):
    return 'This page does not exist', 404

if __name__=="__main__":
    app.run(debug=True)