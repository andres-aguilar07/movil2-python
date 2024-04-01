from flask import Flask, request, redirect, render_template
from config.db import app

#trabajar en las rutas de bluprint con respectos a las api's
from api.UserApi import ruta_user

app.blueprints(ruta_user, url_prefix="/api")

#config el servidor

@app.route("/")
def index():
    return "hola"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')