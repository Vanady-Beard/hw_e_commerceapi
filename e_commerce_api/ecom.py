from flask import Flask,request, jsonify 
# from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow   
# from marshmallow import fields, ValidationError 
from connection import connect_database, db
from customer import Customer, Product, customer_schema, customers_schema, product_schema, products_schema
from mysql.connector import Error



app = Flask(__name__)

ma = Marshmallow(app)
# db.init_app(app)

db = connect_database()


@app.route("/")
def home():
    # print("This will show up in my terminal")
    return " <h1>Welcome To E-commerce Shopping </h1>"


@app.route("/create_account", methods=["Post"])

def add_customer():
    try:
        new_customer = Customer(
             
            name=request.json['name'],
            email=request.json['email'],
            phone=request.json['phone']
        )

        db.session.add(new_customer)
        db.session.commit()
        return customer_schema.jsonify(new_customer), 201
    except Error as e:
        return jsonify({"message": str(e)}), 400
    
@app.post("/update_account")
def update_account():
    try:
        customer_id = request.form['customerID']
        customer = Customer.query.get(customer_id)
        if customer:
            customer.name = request.form['name']
            customer.email = request.form['email']
            customer.phone = request.form['phone']
            
            db.session.commit()
            return customer_schema.jsonify(customer), 200
        else:
            return jsonify ({"message: Customer not found"}), 400
    except Error as e:
         return jsonify({"message": str(e)}), 400
    
    
@app.get("/customers")
def get_customers():
    try:
        customers = Customer.query.all()
        return customers_schema.jsonify(customers), 200

    except Error as e:
        return jsonify({"message": str(e)}), 500
    
@app.post("/products")
def add_products():
    try:

        new_product = Product(name=request.json['name'], 
                              price=request.json["price"])
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify(new_product), 201
    except Error as e:
        return jsonify({"message": str(e)}), 400

@app.get("/products")
def get_products():
    try:
        products = Product.query.all()
        return products_schema.jsonify(products), 200
    except Error as e:
        return jsonify({"message": str(e)}), 500   





if __name__ == "__main__":
    app.run(debug=True )