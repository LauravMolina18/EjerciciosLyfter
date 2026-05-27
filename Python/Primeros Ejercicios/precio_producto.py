product_price=int(input("Ingrese el precio del producto: "))
if product_price < 100:
    discount=product_price * 0.02
else:
    product_price >= 100
    discount=product_price * 0.10
final_price=product_price-discount

print(f"El precio final del producto es: {final_price}")