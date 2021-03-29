from .import bp as shop_bp
from flask import render_template, request, current_app as app, jsonify, session
from flask_login import login_user, current_user, logout_user, login_required
from app.blueprints.shop.models import Product
from app import db

@shop_bp.route('/')
def home():
    context = {
        'products': Product.query.all()
    }
    return render_template('shop/home.html', **context)

@shop_bp.route('/create_product', methods = ["GET", "POST"]) 
@login_required
def create_product():
    if request.method == 'POST':
        res = request.form
        p = Product(name=res['name'], description=res['description'], price=res['price'])
        p.save()
        return render_template('shop/create_product.html')
    return render_template('shop/create_product.html')
#look at how registration page relates to registration view. name area of the form has the name

# @shop_bp.route('/edit_product_select')
# @login_required
# def edit_product_select():
#     return render_template('shop/edit_product_select.html')

# @shop_bp.route('/edit_product')
# @login_required
# def edit_product():
#     return render_template('shop/edit_product.html')


@shop_bp.route('/remove_product', methods=['GET'])
@login_required
def find_product():
    if request.method == 'GET':
        product = Product.query.all()
        return render_template('shop/remove_product.html', products=product)

@shop_bp.route('/remove_product', methods=['POST'])
@login_required
def remove_product():
    if request.method == 'POST':
        # res = request.form
        id = request.form.get('deleteID')
        print(request.form)
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        product = Product.query.all()
        return render_template('shop/remove_product.html', products=product)
        

    # res = request.form
    # db.session.delete(product)
    # db.session.commit()
        # , products={{'product':product}})
