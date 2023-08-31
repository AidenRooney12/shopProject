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
    brand = brandRepository.select(id)
    shoes = shoeRepository.shoes_by_brand(brands)
    return render_template("locations/show.html", brand = brand , shoes = shoes)


@brands_blueprint.route("/brands", methods=['POST'])
def create_shoe():
    name = request.form['name']
    brand = Brand(name)
    brandRepository.save(brand)
    return redirect('/brands')

@brands_blueprint.route("/brands/<id>/delete", methods=['POST'])
def delete_brands(id):
    brandRepository.delete(id)
    return redirect('/brands')
