pricing_map = {}
pricing_map["audio glass"] = 249.99
pricing_map["audio glasses"] = 249.99
pricing_map["insurance"] = 50
pricing_map["speaker"] = 50
pricing_map["speakers"] = 50
pricing_map["earphone"] = 20
pricing_map["earphones"] = 20
pricing_map["headphone"] = 20
pricing_map["headphones"] = 20
pricing_map["sun glasses"] = 50
pricing_map["sunglasses"] = 50

product_list = []
product_list.append([2, "audio glasses"])
product_list.append([1, "insurance"])
product_list.append([3, "headphones"])

def get_all_product_price(product_list):
    total_price = 0
    for product in product_list:
        total_price = total_price + product[0] * pricing_map[product[1]]
    return total_price

print(get_all_product_price(product_list))

def generate_email_body(name, company, school, email, product_list):
    email_body = "Hi " + name + ", " + "\n" + "    This is Virtual"
    return email_body

print(generate_email_body("Howard Li", "Audio Glasses Inc.", "Univ HS", "howardli07@gmail.com", product_list))





