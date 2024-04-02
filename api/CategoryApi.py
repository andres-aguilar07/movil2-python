from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

from models.CategoryModel import Category, CategorySchema

ruta_category= Blueprint("route_user", __name__)

category_schema = CategorySchema()
category_schema = CategorySchema(many=True) 

@ruta_category.route("/api/categories" , methods=["GET"])
def getAllCategories():
    categories = Category.query.all() 
    result = category_schema.dump(categories)
    return jsonify(result)  

@ruta_category.route('/api/addCategory',methods=['POST'])
def addCategory():  
    namecategory = request.json['namecategory']
    newcategory = Category(namecategory)
    db.session.add(newcategory)
    db.session.commit()
    return "Guardado"
