from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.brands import Brand 
import repositories.brandRepository as brandRepository
import repositories.shoeRepository as shoeRepository

brands_blueprint = Blueprint("locations", __name__)

@brands_blueprint.route("/brands")
def brands():
    brands = brandRepository.select_all() # NEW
    return render_template("brands/index.html", brands = brands)

@brands_blueprint.route("/brands/<id>")
def show(id):
    brands = brandRepository.select(id)
    shoes = shoeRepository.shoes_by_brand(brands)
    return render_template("locations/show.html", brand = brand , shoe = shoe)
