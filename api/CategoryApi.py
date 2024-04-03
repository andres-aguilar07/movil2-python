from flask import Flask, Blueprint, request, redirect, render_template, jsonify, url_for
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

@ruta_category.route("/api/deleteCategory/<id>")
def deleteCategory(id):        
    categoryBd = Category.query.get(id)        
    db.session.delete(categoryBd)                     
    db.session.commit()    
    return "Eliminado con exito"

@ruta_category.route("/updateCategory", methods= ["PUT"])
def updateCategory(): 
    id = request.json['id']
    category = Category.query.get(id)       
    category.namecategory = request.json['namecategory']                           
    db.session.commit()                        
    return "Actualizado exitosamente"   
#Vistas para el admin de categorias

@app.route("/admin/categories", methods = ['GET' , 'POST'])
def admin_categories():
    if request.method == 'POST': 
        action = request.form['action']
        id = int(request.form['id'])
        if action == 'Delete':
            flash('La Categoria se ha eliminado correctamente','success')                        
            return redirect(url_for("admin_categories"))                        
        elif action == 'Edit': 
            category = Category.query.filter_by(id=id).first()                        
            return render_template('forms/admin-categories.html', form=category, action='Editar')                        
        else: #Add
            category = Category()             
    else:                     
        category = Category.query.order_by(Category.namecategory).all()             
    return render_template("adminCategories.html", categories=category, action=action)
if __name__ == '__main__':
    app.run(debug=True)     


