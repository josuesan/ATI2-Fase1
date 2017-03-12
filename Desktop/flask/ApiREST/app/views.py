#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, escape
import os, json
from bson import json_util
from bson.objectid import ObjectId
from flask_sqlalchemy import SQLAlchemy
from app.models.users import Users
from app.models.products import productos
from app import app, db
db.create_all()

#db.session.add()
#db.session.commit()
@app.route('/')
def home(): 
	return render_template('home.html')

@app.route("/login", methods = ['GET', 'POST'])
def log_user():
	if request.method == 'POST':
		user = Users()
		usuario = request.form['usuario']
		clave = request.form['clave']
		if user.exist_user(usuario,clave):
			respuesta = {'error':False,'mensaje':'Usuario logueado'}
			return json.dumps(respuesta)

		else:
			respuesta = {'error':True,'mensaje':'Contrasena o Usuario incorrectos'} 
			return json.dumps(respuesta)
	return render_template('login.html') 
        

@app.route('/registro', methods = ['GET', 'POST'])
def Register():
	if request.method == 'POST':
		user = Users()
		user.create_user(request.form['username'],
					request.form['email'],
					request.form['password'],
					request.form['name'],
					request.form['lastname'])
		db.session.add(user)
		db.session.commit()
		if user.exist_user(request.form['username'],request.form['password']):
			respuesta = {'error':False,'mensaje':'Usuario registrado'}
			return json.dumps(respuesta)
		else:
			respuesta = {'error':True,'mensaje':'Contrasena o Usuario incorrectos'} 
			return json.dumps(respuesta)	
	return render_template('registro.html')

@app.route('/listar', methods = ['GET'])
def list():
	prod =productos()
	lista = prod.all_prod()
	number = prod.number_prod()
	jsona = prod.convert(lista,number)
	return json.dumps(jsona)

@app.route('/listar/<ide>', methods = ['GET'])
def part(ide):
	_id = ide
	prod =productos()
	oneProd = prod.get_prod(_id)
	return json.dumps(oneProd)

#@app.route('/editar/', methods = ['GET'])
#def ViewEditar():
	#return render_template('editar_producto.html')

#@app.route('/editar/<ide>', methods = ['PUT'])
#def edit(ide):
	#_id = ide	
	#prod =productos()
	#oneProd = prod.set_prod(_id,request.form['precio'])
	#db.session.commit()
	#return json.dumps(oneProd)

@app.route('/borrar/<ide>', methods = ['GET'])
def delete(ide):
	_id = ide	
	prod =productos()
	oneProd = prod.delete_prod(_id)
	db.session.delete(oneProd)
	db.session.commit()
	respuesta = {'error':False,'mensaje':'Producto Borrado'}
	return json.dumps(respuesta)

@app.route('/crear', methods = ['GET','POST'])
def create():	
	if request.method == 'POST':
		oneProd =productos()
		oneProd.create_prod(request.form['nombre'],request.form['precio'])
		db.session.add(oneProd)
		db.session.commit()
		respuesta = {'error':False,'mensaje':'Producto Creado'}
		return json.dumps(respuesta)

	return render_template('addProduct.html')