friends = ["Ahmad", "All", "Hassan"]
for friend in friends:
    print("As-Salaam-Alaikum", friend)



cart = [
{"item": "Apple", "price": 0.5, "quantity": 4},
{"item": "Banana", "price": 0.2, "quantity": 10},
{"item": "Orange", "price": 0.75, "quantity": 3}
]
total_price = 0
for product in cart:
                item_total = product["price"] * product["quantity"]
                total_price += item_total
                print(f"{product['item']} total: ${item_total:.2f}")
print ("Total price of all items: ${total_price:.2 f}")