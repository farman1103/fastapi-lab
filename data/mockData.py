import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("mockData.json")

with DATA_FILE.open(encoding="utf-8") as file:
    products = json.load(file)


def save_products(product_list):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(product_list, file, indent=4)