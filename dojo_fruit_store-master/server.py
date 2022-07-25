from unicodedata import name
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    frutas = [request.form["strawberry"],request.form["raspberry"],request.form["apple"],request.form["blackberry"]]
    print(f"Cobrando a nombre de {request.form['first_name']} {request.form['last_name']} por {sum(map(int,frutas))} frutas")
    print(request.form)
    return render_template("checkout.html", strawberry=request.form["strawberry"],raspberry=request.form["raspberry"],apple=request.form["apple"],blackberry=request.form["blackberry"], first_name=request.form['first_name'],last_name=request.form['last_name'],student_id=request.form['student_id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    