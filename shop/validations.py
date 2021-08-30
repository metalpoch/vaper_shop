def remaining_products(product_stock, quantity):
    empty_stock = True if product_stock == 0 else False
    can_buy = True if product_stock >= quantity else False
    remaining_product = product_stock if product_stock < quantity else False

    return empty_stock, can_buy, remaining_product
