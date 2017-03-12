from flask_sqlalchemy import SQLAlchemy
import datetime

from app import db

class Users(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(50),unique=True)
	email = db.Column(db.String(40),unique=True)
	password = db.Column(db.String(50))
	name = db.Column(db.String(50))
	lastName = db.Column(db.String(50))


	def create_user(self, username, email, password, name, lastName):
		self.name = name
		self.lastName = lastName
		self.email = email
		self.username = username
		self.password = password
	def exist_user(self, username, pwd):		
		aux = Users.query.filter_by(username=username,password=pwd).first()
		if aux is None:
			return 0
		return 1
	