from db.run_sql import run_sql
from models.shoes import Shoe
from models.brands import Brand

def save(shoe):
    sql = "INSERT INTO shoes( name ) VALUES ( %s ) RETURNING id"
    values = [shoe.name]
    results = run_sql(sql, values )
    shoe.id = results[0]['id']
    return shoe

def select_all():
    shoes = []
    sql = "SELECT * FROM shoes"
    results = run_sql(sql)
    for row in results:
        shoe = Shoe(row['name'], row['id'])
        shoes.append(shoe)
    return shoes


def select(id):
    shoe = None
    sql = "SELECT * FROM/ `` shoes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        shoes = Shoe(result['name'], result['id'] )
    return shoes


def delete_all():
    sql = "DELETE FROM shoes"
    run_sql(sql)

def update(shoe):
    sql = "UPDATE users SET (name, category, buyingCost, sellingCost, numberOfShoes, brand) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [shoe.name, shoe.category, shoe.buyingCost, shoe.sellingCost, shoe.numberOfShoes, shoe.brand, shoe.id]
    run_sql(sql, values)
