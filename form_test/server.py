from flask import Flask, render_template, request,redirect
app = Flask(__name__)

@app.route('/')
def pag_inicial():
    return render_template("index.html")

@app.route('/usuarios',methods=['POST'])
def crear_usuario():
    print("Obtener información")
    print(request.form)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__=="__main__":
    app.run(debug=True)