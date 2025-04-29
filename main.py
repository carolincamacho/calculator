from flask import Flask, request
from operaciones import sumar, restar, dividir, multiplicar
import random

app = Flask(__name__)

@app.route("/")
def home ():
    return '''
        <h1> Proyecto Aplicacion Web con Flask </h1>

        <h2> Calculadora Sencilla</h2>

        <p>Selecciona la operación que desees realizar:</p>
        <ul>
            <li><a href="/suma?num1&num2"> Opción para Sumar </a></li>
            <li><a href="/resta?num1&num2"> Opción para Restar </a></li>
            <li><a href="/divide?num1&num2"> Opción para Dividir </a></li>
            <li><a href="/multiplica?num1&num2"> Opción para Multiplicar </a></li>
        </ul>
    '''

@app.route("/suma")
def suma():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2>la suma de los numeros {num1} y {num2} es: {sumar(num1,num2)}</h2></p>" ''' <p><a href=/><h2> Volver </h2></a></p> 
            '''

@app.route("/resta")
def resta():
    num1=random.randint(1,1000000)
    num2=random.randint(1,1000000)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"<p><h2>la resta de los numeros {num1} y {num2} es: {restar(num1,num2)}</h2></p>" ''' <p><a href=/><h2> Volver </h2></a></p> 
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
