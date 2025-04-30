from flask import Flask, request, render_template
from operaciones import sumar, restar, dividir, multiplicar
import random
from livereload import Server

app = Flask(__name__)

@app.route("/")
def home ():
    return render_template('home.html')

@app.route("/suma")
def suma():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2> La suma de los numeros {num1} y {num2} es: {sumar(num1,num2)}</h2></p>" ''' <p><a href=/><h2> Volver </h2></a></p> 
            '''

@app.route("/resta")
def resta():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2>Para la resta de los numeros {num1} y {num2} es: {restar(num1,num2)}</h2></p>" ''' <p><a href=/><h2> Volver </h2></a></p> 
            '''

@app.route("/divide")
def divide():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2>la division de los numeros {num1} y {num2} es: {dividir(num1,num2)}</h2></p>" ''' <p><h2><a href=/> Volver </a></h2></p> 
            '''

@app.route("/multiplica")
def multiplica():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2>la multiplicación de los numeros {num1} y {num2} es: {multiplicar(num1,num2)}</h2></p>" ''' <p><h2><a href=/> Volver </a></h2></p> 
            '''

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
