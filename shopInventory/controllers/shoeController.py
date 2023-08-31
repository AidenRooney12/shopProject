from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.shoes import Shoe
import repositories.shoeRepository as shoeRepository
import repositories.brandRepository as brandRepository

shoes_blueprint = Blueprint("shoes", __name__)

@shoes_blueprint.route("/shoes")
def shoes():
    shoes = shoeRepository.select_all() # NEW
    print(shoes)
    return render_template("shoes/index.html", shoes = shoes)

@shoes_blueprint.route("/shoes/<id>")
def show(id):
    shoe = shoeRepository.select(id)
    return render_template("shoes/show.html", shoe = shoe)

@shoes_blueprint.route("/shoes/new")
def new():
    brands = brandRepository.select_all()
    return render_template("shoes/new.html", brands = brands)


@shoes_blueprint.route("/shoes", methods=['POST'])
def create_shoe():
    name = request.form['name']
    category = request.form['category']
    buyingCost = request.form['buyingCost']
    sellingCost = request.form['sellingCost']   
    numberOfShoes = request.form['numberOfShoes'] 
    brand = request.form['brand']                 
    brand = brandRepository.select(brand)
    shoe = Shoe(name, category, buyingCost, sellingCost, numberOfShoes, brand)
    shoeRepository.save(shoe)
    return redirect('/shoes')

@shoes_blueprint.route("/shoes/<id>/delete", methods=['POST'])
def delete_shoes(id):
    shoeRepository.delete(id)
    return redirect('/shoes')















