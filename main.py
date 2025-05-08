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
    resultado=sumar(num1,num2)
    return render_template('suma.html',resultado=resultado,num1=num1,num2=num2)

@app.route("/resta")
def resta():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    resultado=restar(num1,num2)
    return render_template("resta.html",resultado=resultado,num1=num1,num2=num2)
    
@app.route("/divide")
def divide():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    ''' asi era el codigo antes de utilizar archivos html
    return f"<p><h2>la division de los numeros {num1} y {num2} es: {dividir(num1,num2)}</h2></p>" ''' 
    '''<p><h2><a href=/> Volver </a></h2></p> '''
    resultado=dividir(num1,num2)
    return render_template("divide.html",resultado=resultado,num1=num1,num2=num2)

@app.route("/multiplica")
def multiplica():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h1>Calculadora con codigo sin html</h1></p><p><h2>la multiplicación de los numeros {num1} y {num2} es: {multiplicar(num1,num2)}</h2></p>"''' <p><h2><a href=/> Volver </a></h2></p> '''

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
