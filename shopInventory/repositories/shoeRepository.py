from db.run_sql import run_sql
from models.shoes import Shoe
from models.brands import Brand
import repositories.brandRepository as brandRepository


def save(shoe):
    sql = "INSERT INTO shoes( name, category, buying_cost, selling_cost, number_of_shoes, brand_id) VALUES ( %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [shoe.name, shoe.category, shoe.buyingCost, shoe.sellingCost, shoe.numberOfShoes, shoe.brand.id]
    results = run_sql(sql, values )
    shoe.id = results[0]["id"]
    return shoe

def select_all():
    shoes = []
    sql = "SELECT * FROM shoes"
    results = run_sql(sql)
    for row in results:
        brand = brandRepository.select(row["brand_id"]) 
        shoe = Shoe(row["name"], row["category"], row["buying_cost"], row["selling_cost"], row["number_of_shoes"],  brand, row["id"])
        shoes.append(shoe)
        print(shoe)
    return shoes


def select(id):
    shoe = None
    sql = "SELECT * FROM shoes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        print(result)
        brand = brandRepository.select(result["brand_id"]) 
        print(brand)
        shoe = Shoe(result["name"], result["category"], result["buying_cost"], result["selling_cost"], result["number_of_shoes"],  brand, result["id"])
        print(shoe)
    return shoe


def delete_all():
    sql = "DELETE FROM shoes"
    run_sql(sql)

def update(shoe):
    sql = "UPDATE users SET (name, category, buying_cost, selling_cost, number_of_shoes, brand) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [shoe.name, shoe.category, shoe.buyingCost, shoe.sellingCost, shoe.numberOfShoes, shoe.brand, shoe.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM shoes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def shoes_by_brand(brand):
    shoes = []
    sql = "SELECT * FROM shoes WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)
    for row in results:
        brand = brandRepository.select(row["brand_id"]) 
        shoe = Shoe(row["name"], row["category"], row["buying_cost"], row["selling_cost"], row["number_of_shoes"],  brand, row["id"])
        shoes.append(shoe)
    return shoes

