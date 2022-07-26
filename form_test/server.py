from flask import Flask, render_template, request,redirect, session
app = Flask(__name__)
app.secret_key="Laurelin y Telperion ajá"

@app.route('/')
def pag_inicial():
    return render_template("index.html")

@app.route('/usuarios',methods=['POST'])
def crear_usuario():
    print("Obtener información")
    print(request.form)
    session["name"] = request.form['name']
    session["email"] = request.form['email']
    return redirect('/show')

@app.route('/show')
def mostar_usuario():
    return render_template("show.html")


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__=="__main__":
    app.run(debug=True)