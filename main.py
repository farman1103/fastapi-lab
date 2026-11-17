from fastapi import FastAPI, Request
from data.mockData import products, save_products
from schema.product import ProductSearch, AddProduct

app = FastAPI()

@app.get("/")
def home():
    return {"Welcome to the FastAPI application!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Get All Products --
@app.get("/products")
def get_all_products():
    return products 

# Query Parameter Example --
@app.get("/products/search")
def get_products_by_value(min_price: int, max_price: int):
    filtered_products = []
    for product in products:
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

# Post Request Example --
@app.post("/products/add")
def add_product(product: AddProduct):
    product_dict = product.model_dump()
    products.append(product_dict)
    save_products(products)
    return {"message": "Product added successfully", "product": product}

# Put Request Example --
@app.put("/products/update")
def update_product(product: AddProduct):
    for i, p in enumerate(products):
        if p["id"] == product.id:
            products[i] = product.model_dump()
            save_products(products)
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}

# Delete Request Example --
@app.delete("/products/delete/{product_id}")
def delete_product(product_id: int):
    global products
    products = [product for product in products if product["id"] != product_id]
    save_products(products)
    return {"message": "Product deleted successfully"}