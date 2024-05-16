from usuarios_app import app
from flask import Flask

from usuarios_app.controladores import controlador_usuarios, controlador_api, controlador_departamentos

if __name__ == "__main__":
    app.run(debug=True)