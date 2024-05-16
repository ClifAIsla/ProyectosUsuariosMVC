from flask import Flask,request, redirect, session, jsonify, json
from usuarios_app import app
from usuarios_app.modelos.modelo_usuarios import Usuario
# from flask_bcrypt import Bcrypt 
#OJO NO TE OLVIDES IMPORTAR bcrypt -> pipenv install flask-bcrypt

# bcrypt = Bcrypt(app)

#EN EL API MI OBJETIVO NO ES GENERAR UN HTML SINO UN JSON, POR ESO NO IMPORTO RENDER_TEMPLATE

#STATUS 201 PARA CREAR OBJETOS
#STATUS 200 PARA OBTENER OBJETOS

#RUTAS
@app.route('/api/usuarios', methods=['GET'])
def obtenerlistaUsuarios():
    listaUsuarios = Usuario.obtenerAllUsuariosAPI()
    print("SOLO ACEPTA LISTA DE DICCIONARIO: ",listaUsuarios)
    return jsonify( listaUsuarios ),200

@app.route('/api/usuarios/crear',methods=['POST'])
def agregaUsuario():
    #OJO, AQUI NO USAMOS .form SINO .data XQ Y AGREGAMOS UNA CODIFICACION
    # print( request.form ) 
    
    #POR ULTIMO, EL .data.decode('UTF-8') NOS DEVUEVE UN STRING, ENTONCES LO FORZAMOS A SER UN DICCIONARIO
    nuevoUsuario = json.loads( request.data.decode('UTF-8') )
    print(nuevoUsuario)
    # passwordEncriptado = bcrypt.generate_password_hash( nuevoUsuario["password"] )
    # nuevoUsuario["password"] = passwordEncriptado
    # print(nuevoUsuario)
    Usuario.agregaUsuario(nuevoUsuario)
    return jsonify({"mensaje" : "Usuario creado exitossmaente"}),201

@app.route('/api/usuarios/eliminar/<nombreUsuario>',methods=['DELETE'])
def eliminarUsuarioAPI( nombreUsuario ):
    usuarioEliminar = {
        "nombreUsuario" : nombreUsuario
    }

    #VALIDACION PARA ELIMINAR UN ELEMENTO QUE SI EXISTE
    existeUsuario = Usuario.obtenerDatosUsuarios(usuarioEliminar)
    if len(existeUsuario) == 0:
        return jsonify({"mensaje":"Ese usuario no existe"}),404
    else:    
        Usuario.removerUsuario(usuarioEliminar)
        return jsonify({}),204

# @app.route('/api/usuarios/acualizar', methods=["PUT"])
