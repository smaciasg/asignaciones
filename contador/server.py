from ast import Not
from asyncio.windows_events import NULL
from genericpath import exists
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Arboles Telperion y Laurelin"

lista_ingresos = []
lista_contar=[]
lista_valor_incremeto = []
@app.route('/')
def index():
    global lista_ingresos,lista_valor_incremeto,lista_contar
    session['contadorindex'] = len(lista_ingresos)
    if session is not NULL:
        session['contadorindex'] += 1
        lista_ingresos.append(session['contadorindex'])
    session['contadorcontar'] = lista_ingresos[len(lista_ingresos)-1]
    return render_template("index.html")

@app.route('/cuenta', methods=['POST'])
def contador():
    session['val_invrement']=request.form['val_invrement']
    lista_valor_incremeto.append(session['val_invrement'])
    return redirect('/contador')

@app.route('/limpiar') ## Mi versión de destroy_session
def limpiar():
    session.clear()
    lista_ingresos.clear()
    lista_contar.clear()
    lista_valor_incremeto.clear()
    return redirect('/')

@app.route('/contador')
def contar_user():
    if session is not NULL:
        if int(len(lista_valor_incremeto)) == 1:
            session['contadorcontar'] += int(lista_valor_incremeto[0])
            lista_contar.append(session['contadorcontar'])
        elif lista_valor_incremeto[int(len(lista_valor_incremeto))-1]== "":
            x=0
            for i in lista_valor_incremeto:
                if i != "" and int(i) >0:
                    x=int(i)
            session['contadorcontar'] += int(x)
            lista_contar.append(session['contadorcontar'])
        elif lista_valor_incremeto[int(len(lista_valor_incremeto))-1]!= "":
            session['contadorcontar'] += int(lista_valor_incremeto[int(len(lista_valor_incremeto))-1])
            lista_contar.append(session['contadorcontar'])
        session['cantidad_click'] = session['contadorcontar'] - session['contadorindex']
    return render_template("contador.html")

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__=="__main__":
    app.run(debug=True)