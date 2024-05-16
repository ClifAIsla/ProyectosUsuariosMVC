from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__(self,nombre,apellido,nombreUsuario,password,id_departamento):
        self.nombre = nombre
        self.apellido=apellido
        self.nombreUsuario=nombreUsuario
        self.password=password
        self.id_departamento=id_departamento
    
    @classmethod
    def agregaUsuario(cls,nuevoUsuario):
        query = "INSERT into usuarios(nombre,apellido,nombreUsuario,password,id_departamento) VALUES(%(nombre)s,%(apellido)s,%(nombreUsuario)s,%(password)s,%(id_departamento)s)"
        resultado=connectToMySQL("usuarios_db").query_db(query,nuevoUsuario)
        print(resultado)
        return resultado
        
    @classmethod
    def darAcceso(cls,usuario):
        query = "SELECT * FROM usuarios WHERE nombreUsuario=%(nombreUsuario)s AND password=%(password)s"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuario)
        if len(resultado)>0:
            usuarioEncontrado = Usuario (resultado[0]["nombre"],resultado[0]["apellido"],resultado[0]["nombreUsuario"],resultado[0]["password"],resultado[0]["id_departamento"])
            return usuarioEncontrado
        else:
            return None
        
    @classmethod
    def obtenerAllUsuarios(cls):
        query = "SELECT * FROM usuarios"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        listaUsuarios=[]
        for usuario in resultado:
            nuevoUsuario = Usuario(usuario['nombre'],usuario['apellido'],usuario['nombreUsuario'],usuario['password'],usuario['id_departamento'])
            listaUsuarios.append(nuevoUsuario)
        return listaUsuarios
        
    @classmethod
    def removerUsuario(cls,usuarioEliminar):
        query = "DELETE FROM usuarios WHERE nombreUsuario=%(nombreUsuario)s;"
        # return connectToMySQL("usuarios_db").query_db(query)
        return connectToMySQL("usuarios_db").query_db(query,usuarioEliminar)

    @classmethod
    def buscarUnUsuario(cls,usuarioBuscado):
        query = "SELECT * FROM usuarios WHERE nombreUsuario=%(nombreUsuario)s"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuarioBuscado)
        print("LO ENCONTRO: ",resultado[0])
        return resultado[0]
    
    @classmethod
    def obtenerDatosUsuarios(cls,usuarioBuscado):
        query = "SELECT * FROM usuarios WHERE nombreUsuario=%(nombreUsuario)s"
        return connectToMySQL("usuarios_db").query_db(query,usuarioBuscado)
    
    @classmethod
    def actualizarUsuario(cls,usuarioActualizar):
        query = "UPDATE usuarios SET nombre = %(nombre)s, apellido=%(apellido)s, password=%(password)s, id_departamento=%(id_departamento)s WHERE nombreUsuario = %(nombreUsuario)s;"
        resultado = connectToMySQL("usuarios_db").query_db(query,usuarioActualizar)
        print("actualizar: ","%(nombreUsuario)s")
        return resultado

    @classmethod
    def obtenerAllUsuariosAPI(cls):
        query = "SELECT * FROM usuarios"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        return resultado
        # listaUsuarios=[]
        # for usuario in resultado:
        #     nuevoUsuario = Usuario(usuario['nombre'],usuario['apellido'],usuario['nombreUsuario'],usuario['password'],usuario['id_departamento'])
        #     listaUsuarios.append(nuevoUsuario)
        # return listaUsuarios


#OJO ES IMPORTANTE ENVIARLE UN DICCIONARIO, EN EL QUERY