from flask import Flask,render_template,request, redirect, session
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario
import random

#Rutas
@app.route('/',methods=["GET"])
def despliegaRegistroLogin():
    return render_template("index.html")
    
@app.route('/dashboard',methods=['GET'])
def despliegaDashboard():
    if 'nombre' in session:

        listaUsuarios=Usuario.obtenerAllUsuarios()
        print("ARREGLO OBJETOS: ",listaUsuarios)


        return render_template("dashboard.html",usuarios=listaUsuarios)
    else:
        return redirect("/")

@app.route('/registroUsuario',methods=['POST'])
# COMO VAMOS A OBTENER VALORES DEL FORMULARIO USAMOS REQUEST
def regitrarUsuario():

    #OJITO, LOS JALA CON SU ID
    nuevoUsuario = {
        #OJITO EL NOMBRE DEL DICCIONARIO ES IGUAL AL DEL MYSQL
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "nombreUsuario" : request.form['usuario'],
        "password" : request.form['password'],
        "id_departamento" : request.form['departamento']
    }

    #COMO SERIA USANDO EL CONTROLADOR
    resultado = Usuario.agregaUsuario(nuevoUsuario)
    if resultado == False:
        return redirect('/')
    else:

        print(resultado)
    # print(request.form)

        session['nombre'] = request.form['nombre']
        session['apellido'] = request.form['apellido']

        return redirect ('/dashboard')

@app.route('/login', methods=['POST'])
def loginUsuario():

    usuario = {
        "nombreUsuario" : request.form['usuarioLogin'],
        "password" : request.form['passwordLogin']
    }

    usuarioEncontrado = Usuario.darAcceso(usuario)
    print(usuarioEncontrado)

    if usuarioEncontrado == None:
        return redirect('/')
    else:
        session["nombre"] = usuarioEncontrado.nombre
        return redirect('/dashboard')

@app.route('/usuario/eliminar/<nombreUsuario>', methods=["POST"])
def eliminarUsuario(nombreUsuario):
    usuarioEliminar = {
        "nombreUsuario" : nombreUsuario
    }
    print(nombreUsuario)
    Usuario.removerUsuario(usuarioEliminar)
    return redirect("/dashboard")

@app.route('/usuario/editar/<nombreUsuario>', methods=["GET"])
def editarUsuario(nombreUsuario):

    usuarioEncontrado = {
        "nombreUsuario" : nombreUsuario
    }
    usuarioActualizar = Usuario.buscarUnUsuario(usuarioEncontrado)
    return render_template("editarUsuario.html",usuarioActualizar=usuarioActualizar)

@app.route('/usuario/editar/<nombreUsuario>', methods=["POST"])
def actualizarUsuario(nombreUsuario):

    datosActualizar = {
        "nombre" : request.form['nombre'],
        "apellido" : request.form['apellido'],
        "nombreUsuario" : nombreUsuario,
        "password" : request.form['password'],
        "id_departamento" : request.form['departamento']
    }
    Usuario.actualizarUsuario(datosActualizar)
    return redirect("/dashboard")

@app.route('/logout',methods=['GET'])
def logOut():
    session.clear()
    return redirect('/')