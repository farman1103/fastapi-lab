from pydantic import BaseModel

class ProductSearch(BaseModel):
    min_price: int
    max_price: int
    brand: str