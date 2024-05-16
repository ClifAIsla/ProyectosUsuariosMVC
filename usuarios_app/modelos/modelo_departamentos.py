from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from usuarios_app.modelos.modelo_usuarios import Usuario

class Departamento:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.usuario = []

    def agregaUsuario(self,usuario):
        self.usuario.append(usuario)

    @classmethod
    def obtenerListaDepartamentos(cls):
        query = "SELECT * FROM departamentos"
        resultado = connectToMySQL("usuarios_db").query_db(query)
        # print("resultado :",resultado)
        listaDepartamentos = []
        for departamento in resultado:
            listaDepartamentos.append( cls(departamento['id'],departamento['nombre']))
            # print("departamento :",departamento)
        return listaDepartamentos
        # print("listaDepartamentos :",listaDepartamentos)

    @classmethod
    def obtenerListaDepartamentosConUsuarios(cls):
        query = "SELECT * FROM departamentos d, usuarios u WHERE d.id=u.id_departamento"
        resultado = connectToMySQL("usuarios_db").query_db(query)

        listaDepartamentosConUsuario = []

        for reglon in resultado:
            indice = existeDepartamentoEnArreglo( reglon['id'] , listaDepartamentosConUsuario )
            print("indice",indice)

            if indice == -1:
                #EL DEPORTAMENTO NO EXISTE EN NUESTRA LISTADEPARTAMENTOS, LO VAMOS A DAR DE ALTA
                departamentoAAgregar = Departamento(reglon['id'],reglon['nombre'])
                departamentoAAgregar.agregaUsuario( Usuario(reglon['u.nombre'],reglon['apellido'],reglon['nombreUsuario'],reglon['password'],reglon['id_departamento']) )
                listaDepartamentosConUsuario.append( departamentoAAgregar )

            else:
                #SI EL INDICE YA EXISTIA, SOLO AGREGAMOS AL USUARIO
                # for departamento in listaDepartamentosConUsuario:
                #     departamento['id'] =reglon['id']:
                print('listaDepartamentos :',listaDepartamentosConUsuario)
                listaDepartamentosConUsuario[indice].agregaUsuario(Usuario(reglon['u.nombre'],reglon['apellido'],reglon['nombreUsuario'],reglon['password'],reglon['id_departamento']) )

        return listaDepartamentosConUsuario
        

def existeDepartamentoEnArreglo(id_departamento,listaDepartamentos):

    for i in range(0,len(listaDepartamentos)):
        if listaDepartamentos[i].id == id_departamento:
            return i
    return -1
        
#AQUI HAY UN ERROR REVISAR

