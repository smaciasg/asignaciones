from random import random,randint
from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "Este debe ser seguro"

lista_ganadores = []
@app.route('/')
def pag_inicial():
    # session.clear()
    session['aleatrio'] = randint(1,100)
    session['contar_intentos'] = 5
    return render_template('mostar_num.html')

@app.route('/validar_num', methods=['POST'])
def validar_num():
    session['numero']=int(request.form["numero"])
    print(session['aleatrio'], session['numero'])
    while session['contar_intentos'] >1:
        if session['numero'] == session['aleatrio']:
            session['texto'] = "Ganaste"
            session['contar_intentos'] -=1
            print(session['contar_intentos'])
            return redirect('/index')
        elif session['numero'] > session['aleatrio']:
            session['texto'] = "Muy alto"
            session['contar_intentos'] -=1
            print(session['contar_intentos'])
            return redirect('/index')
        elif session['numero'] < session['aleatrio']:
            session['texto'] = "Muy bajo"
            session['contar_intentos'] -=1
            print(session['contar_intentos'])
            return redirect('/index')
    else:
        if session['numero'] == session['aleatrio']:
            session['texto'] = "Ganaste"
            session['contar_intentos'] -=1
            print(session['contar_intentos'])
            return redirect('/index')
        else:  
            return redirect('/perdio')

@app.route('/index')
def retornar():
    return render_template('index.html')

@app.route('/perdio')
def perdio():
    return render_template('perdio.html')

@app.route('/registro_ganador')
def registro():
    return render_template('registro_ganador.html')

@app.route('/listado_ganadores', methods=['POST'])
def listado_ganadores():
    users = request.form
    lista_ganadores.append(users)
    session['lista_jugadores'] = lista_ganadores
    print(session['lista_jugadores'])
    return redirect('/mostrar_ganadores')

@app.route('/mostrar_ganadores')
def mostrar_ganadores():
    return render_template('mostrar_ganadores.html')


if __name__=="__main__":
    app.run(debug=True)