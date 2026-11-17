from pydantic import BaseModel

class ProductSearch(BaseModel):
    min_price: int
    max_price: int
    brand: str

class AddProduct(BaseModel):
    id: int
    name: str
    price: int
    quantity: int