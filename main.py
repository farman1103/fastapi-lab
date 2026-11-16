from fastapi import FastAPI, Request
from mockData import products
from schema.product import ProductSearch

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome to the FastAPI application!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Query Parameter Example --
@app.get("/products/search")
def get_products_by_value(min_price: int, max_price: int):
    filtered_products = []
    for product in products:
        if min_price <= product["price"] <= max_price:
            filtered_products.append(product)
    return filtered_products

# Request Body Example --
@app.post("/products/search/request")
def get_products_by_values(iprequest: ProductSearch):
    filtered_products = []
    for product in products:
        if iprequest.min_price is not None and iprequest.max_price is not None:
            min_price = iprequest.min_price
            max_price = iprequest.max_price
            if min_price <= product["price"] <= max_price:
                filtered_products.append(product)
    return filtered_products


# Path Parameter Example --
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

