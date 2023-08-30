from models.brands import Brand
from models.shoes import Shoe


import repositories.brandRepository as brandRepository
import repositories.shoeRepository as shoeRepository

shoe1 = Shoe("Samba", "Low Sneaker", "£60", "£100","10 Units", "Adidas")
shoe2 = Shoe("2002R", "Sneaker", "£150", "£220","40 Units", "New Balance")


brand1 = Brand("Adidas")
brand2 = Brand("New Balance")
