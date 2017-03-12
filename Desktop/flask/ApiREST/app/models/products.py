from flask_sqlalchemy import SQLAlchemy
import datetime
from collections import OrderedDict
import  json
from app import db

class productos(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	nombre = db.Column(db.String(50),unique=True)
	precio = db.Column(db.Integer)


	def create_prod(self, nombre, precio):
		self.nombre = nombre
		self.precio = precio

	def get_prod(self, id):		
		aux = productos.query.filter_by(id=id).first()
		if aux is None:
			return 0
		return {'id':aux.id,'nombre': aux.nombre,'precio':aux.precio}
	def all_prod(self):		
		aux = productos.query.all()
		if aux is None:
			return 0
		return aux
	def number_prod(self):		
		print( productos.query.count())
		return productos.query.count()

	def convert(self, lista, cantidad):
		jsona = [{'id':lista[i].id,'nombre':lista[i].nombre,'precio':lista[i].precio} for i in range(0,cantidad)]
		print(jsona)
		return jsona

	#def set_prod(self, id, precio):		
		#aux = productos.query.get(id)
		#if aux is None:
		#	return 0
		#aux.precio = precio
		#jsona = {'id':aux.id,'nombre':aux.nombre,'precio':aux.precio} 
		#return jsona*/

	def delete_prod(self, id):		
		aux = productos.query.get(id)
		if aux is None:
			return 0 
		return aux 
		
			
