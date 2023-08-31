from models.brands import Brand
from models.shoes import Shoe


import repositories.brandRepository as brandRepository
import repositories.shoeRepository as shoeRepository

shoeRepository.delete_all()
brandRepository.delete_all()

brand1 = Brand("Adidas")
brandRepository.save(brand1)
brand2 = Brand("New Balance")
brandRepository.save(brand2)
brand3 = Brand("Nike")
brandRepository.save(brand3)

shoe1 = Shoe("Samba", "Low Sneaker", "£60", "£100","10 Units", brand1)
shoeRepository.save(shoe1)
shoe2 = Shoe("2002R", "Sneaker", "£150", "£220","40 Units", brand2)
shoeRepository.save(shoe2)
shoe3 = Shoe("Air Max 95", "Sneaker", "£180", "£220", "100 Units", brand3)
shoeRepository.save(shoe3)

brand = brandRepository.select(1)
print(brand)
brands = brandRepository.select_all()
print(brands)

shoe = shoeRepository.select(1)
print(shoe)
shoes = shoeRepository.select_all()
print(shoes)

