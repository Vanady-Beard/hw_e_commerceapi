from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow   
from marshmallow import fields, Schema, ValidationError 
from connection import db
# from mysql.connector import Error

app = Flask(__name__)
ma = Marshmallow(app)


class Customer(db.Model):
    __tablename__ = "Customer"


    customerID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)



class Product (db.Model):
     __tablename__ = 'Product'

     productID = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable = False)
     price = db.Column(db.Float, nullable=False)





class CustomerSchema(ma.Schema):
    customerID = fields.Integer()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)

# class Meta: 
#     fields = ("customerID", "name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class ProductSchema(ma.Schema):
    productID = fields.Integer()
    name = fields.String(required=True)
    price = fields.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


























