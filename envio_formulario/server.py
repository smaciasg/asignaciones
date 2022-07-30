from flask import Flask, redirect,render_template,request,session
app = Flask(__name__)
app.secret_key="Esto debe ser zekreto"


@app.route('/')
def form_inicial():
    return render_template('index.html')

@app.route('/envio',methods=['POST'])
def enviar():
    session['nombre'] = request.form['nombre']
    session['apellido'] = request.form['apellido']
    session['num_hijos'] = request.form['num_hijos']
    session['fecha_nacimiento'] = request.form['fecha_nacimiento']
    session['email'] = request.form['email']
    session['locacion'] = request.form['locacion']
    session['lenguaje_proramacion'] = request.form['lenguaje_proramacion']
    session['envio_info'] = request.form['envio_info']
    if session['envio_info']=="Campos Opcionales":
        return redirect('/')
    else:
        session['envio_info']
        session['user_data'] = request.form
        print(session['user_data'])
        return redirect('/resumen_datos')

@app.route('/resumen_datos')
def mostrar_data():
    return render_template('/resumen_datos.html')

@app.route('/limpiar')    
def index_mas_campos():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)