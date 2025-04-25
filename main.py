from flask import Flask, request
from operaciones import sumar

app = Flask(__name__)

@app.route("/")
def home ():
    return '''
<h1> Proyecto Calculadora </h1>

<a href="/suma?num1=4&num2=20"> Opción para Sumar </a>
'''

@app.route("/suma")
def suma():
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la suma de los numeros es: {sumar(num1,num2)}"
