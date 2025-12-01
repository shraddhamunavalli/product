import pytest
def product_details(name, product_id, quantity, price):
    result = (
        f"product Name: {name}\n"
        f"productID: {product_id}\n"
        f"product quantity: {quantity}\n"
        f"price: {price}"
    )
    return result

if __name__ == "__main__":
    # Sample values
    name = "shampoo"
    product_id = "E1001"
    product_quantity = "3"
    price= 300

    print(product_details(name, product_id, product_quantity, price))