from db.run_sql import run_sql
from models.brands import Brand


def save(brand):
    sql = "INSERT INTO brand( name ) VALUES ( %s ) RETURNING id"
    values = [brand.name]
    results = run_sql(sql, values )
    brand.id = results[0]['id']
    return brand

def select_all():
    brands = []
    sql = "SELECT * FROM brands"
    results = run_sql(sql)
    for row in results:
        brand = Brand(row['name'], row['id'])
        brands.append(brand)
    return brands


def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        brand = Brand(result['name'], result['id'] )
    return brand


def delete_all():
    sql = "DELETE * FROM brands "
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)



def shoes_per_brand(brand):
    shoes = []
    sql = "SELECT * FROM shoes WHERE brand_id = %s"
    values = [brand.id]
    results = run_sql(sql, values)
    for row in results:
        shoes = shoes(row['brand'])
        shoes.append(brand)
    return shoes




