def product_sort():
    products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True], ["Bomb", 30.6, True],
                ["Crown", 37.6, False], ["Plane", 400.30, True], ["Cards", 15.15, True], ["Boats", 1500.30, True]]
    on_sale_products = [product for product in products if product[-1]]
    print(products)
    print(on_sale_products)


def main():
    product_sort()


main()