from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.shoes import Shoe
import repositories.shoeRepository as shoeRepository
import repositories.brandRepository as brandRepository

shoes_blueprint = Blueprint("shoes", __name__)

@shoes_blueprint.route("/shoes")
def shoes():
    shoes = shoeRepository.select_all() # NEW
    return render_template("users/index.html", shoes = shoes)

@shoes_blueprint.route("/shoes/<id>")
def show(id):
    shoe = shoeRepository.select(id)
    brand = brandRepository.brands_by_shoe(shoe)
    return render_template("users/show.html", shoe = shoe, brand = brand)
