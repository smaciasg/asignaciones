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
    if session['envio_data'] == "Granja":
        lista_cantidades.append(session['aleatorio_granja'])
        lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {session['aleatorio_granja']} en la {session['envio_data']}! ({now})</p>")
    elif session['envio_data'] == "Cueva":
        lista_cantidades.append(session['aleatorio_cueva'])
        lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {session['aleatorio_cueva']} en la {session['envio_data']}! ({now})</p>")
    elif session['envio_data'] == "Casa":
        lista_cantidades.append(session['aleatorio_casa'])
        lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {session['aleatorio_casa']} en la {session['envio_data']}! ({now})</p>")
    elif session['envio_data'] == "Casino":
        if session['aleatorio_casino']%5 == 0:
            lista_cantidades.append((-1*session['aleatorio_casino']))
            lista_comentarios.append(f"<p style='color: tomato;'>¡Perdiste {session['aleatorio_casino']} en el {session['envio_data']}! ({now})</p>")
        else:
            lista_cantidades.append(session['aleatorio_casino'])
            lista_comentarios.append(f"<p style='color: yellowgreen;'>¡Ganaste {session['aleatorio_casino']} en el {session['envio_data']}! ({now})</p>")
    session['lista_cantidades'] = lista_cantidades[::-1]
    session['lista'] = lista_comentarios[::-1]
    return redirect('/')

@app.route('/limpiar')
def limpiar():
    session.clear()
    lista_cantidades.clear()
    lista_comentarios.clear()
    session['sum_oro'].clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)