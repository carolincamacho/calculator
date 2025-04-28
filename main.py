from flask import Flask, request
from operaciones import sumar

app = Flask(__name__)

@app.route("/")
def home ():
    return
'''
<h3> Proyecto Aplicacion Web con Flask </h3>

<h2> Calculadora Sencilla</h2>

<p>Selecciona la operación que desees realizar:</p>
<ul>
    <li><a href="/suma"> Opción para Sumar </a></li>
    <li><a href="/resta"> Opción para Restar </a></li>
    <li><a href="/dividir"> Opción para Dividir </a></li>
    <li><a href="/nultiplicar"> Opción para Multiplicar </a></li>
</ul>
<p><a href="/"> Volver </a></p>

'''

@app.route("/suma")
def suma():
    num1=float (input ("favor entregar primer numero: "))
    num2=float (input ("favor entregar segundo numero: "))
    num1=request.args.get("num1", type=float)
    num2=request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "faltan datos"
    return f"la suma de los numeros es: {sumar(num1,num2)}"
    '''
    <p><a href="/"> Volver </a></p>
    '''
