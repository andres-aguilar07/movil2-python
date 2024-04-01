from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

#llamamos al modelo de User
from models.UserModel import Users, UsersSchema

ruta_user = Blueprint("route_user", __name__)

usuario_schema = UsersSchema()
usuarios_schema = UsersSchema(many=True)

@ruta_user.route("/user")
def alluser():
    resultAll = Users.query.all()
    respo = usuarios_schema(resultAll)
    return jsonify(respo)


