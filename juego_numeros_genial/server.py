from random import random,randint
from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "Este debe ser seguro"

@app.route('/')
def pag_inicial():
    session.clear()
    session['aleatrio'] = randint(0,100)
    return render_template('mostar_num.html')

@app.route('/validar_num', methods=['POST'])
def validar_num():
    session['numero']=int(request.form["numero"])
    print(session['aleatrio'], session['numero'])
    if session['numero'] == session['aleatrio']:
        session['texto'] = "Ganaste"
    elif session['numero'] > session['aleatrio']:
        session['texto'] = "Muy alto"
    elif session['numero'] < session['aleatrio']:
        session['texto'] = "Muy bajo"
    return redirect('/index')

@app.route('/index')
def retornar():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)