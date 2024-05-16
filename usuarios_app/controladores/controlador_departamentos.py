from flask import Flask,render_template,request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_departamentos import Departamento

@app.route('/departamentos',methods=['GET'])
def despliegaDepartamento():
    listaDepartamentos = Departamento.obtenerListaDepartamentos()
    # print('HABER: ',listaDepartamentos)
    departamentosConUsuarios=Departamento.obtenerListaDepartamentosConUsuarios()

    return render_template('departamentos.html',listaDepartamentos=listaDepartamentos,departamentosConUsuarios=departamentosConUsuarios)
