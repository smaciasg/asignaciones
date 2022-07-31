from flask import Flask, session,redirect,render_template,request
from random import random,randint
from datetime import datetime
app = Flask(__name__)
app.secret_key = "Esperemos jj.tm no mueran en las mentas 12345874a"

lista_cantidades = [0]
lista_comentarios = [""]
now = datetime.now()
@app.route('/')
def index():
    global lista_cantidades, lista_comentarios, now
    session['aleatorio_granja'] = randint(10,20)
    session['aleatorio_cueva'] = randint(5,10)
    session['aleatorio_casa'] = randint(2,5)
    session['aleatorio_casino'] = randint(0,50)
    session['sum_oro']=sum(lista_cantidades)
    session['intentos_restantes']=15-(len(lista_cantidades))
    return render_template ('index.html')

@app.route('/procesar_oro', methods=['POST'])
def procesar_oro():
    session['envio_data'] = request.form['envio_data']
    dic = {
        "Granja":session['aleatorio_granja'],
        "Cueva":session['aleatorio_cueva'],
        "Casa":session['aleatorio_casa'],
        "Casino":session['aleatorio_casino'],
    }
    for key in dic:
        if key == session['envio_data']:
            if key == "Casino":
                if dic[key]%5 == 0:
                    lista_cantidades.append(-1*(int(dic[key])))
                    lista_comentarios.append(f"<p style='color: tomato;'>Perdiste {dic[key]} en: {key}! ({now})</p>")
                else:
                    lista_cantidades.append(int(dic[key]))
                    lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {dic[key]} en: {key}! ({now})</p>")
            else:
                lista_cantidades.append(int(dic[key]))
                lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {dic[key]} en: {key}! ({now})</p>")
    session['lista_cantidades'] = lista_cantidades[::-1]
    session['lista'] = lista_comentarios[::-1]
    return redirect('/')

@app.route('/limpiar')
def limpiar():
    session.clear()
    lista_cantidades.clear()
    lista_comentarios.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)