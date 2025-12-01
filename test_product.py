from pytest.pytest1.employee import product_details
def test_product_details():
    excepted_output = (
        "product Name: shampoo\n"
        "product ID: E1001\n"
        "product quantity: 3\n"
        "price: 300"
    )
    assert product_details("shampoo","E1001","3",300)== excepted_output
    