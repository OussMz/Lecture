import os


current_dir = os.path.dirname(os.path.abspath(__file__))
products_file_path = os.path.join(current_dir, "products.txt")
print(os.path.abspath(__file__))
print(current_dir)
with open(products_file_path, "w") as f:
    f.write("""Laptop Computer,999.99,Electronics,Premium
Winter Jacket,129.99,Clothing,Standard
Python Programming Book,49.99,Books,Standard
Coffee Maker,79.99,Home,Budget
Wireless Headphones,199.99,Electronics,Premium""")
    
print("Products Information:\n")

with open(products_file_path) as f:
    try:
        total_products = 0
        total_discount_applied = 0
        for line in f:
            total_products += 1
            name, base_price, category, tier = line.strip().split(",")
            base_price = float(base_price)
            if category == "Electronics":
                category_discount = 10
            elif category == "Clothing":
                category_discount = 15
            elif category == "Books":
                category_discount = 5
            elif category == "Home":
                category_discount = 12
            else:
                category_discount = 0

            if tier == "Premium":
                tier_discount = 5
            elif tier == "Budget":
                tier_discount = 2
            else:
                tier_discount = 0
            
            total_discount_percentage = (100*(category_discount + tier_discount)-(category_discount * tier_discount))/100
            total_discount_applied += total_discount_percentage
            discount_amount = (total_discount_percentage/100) * base_price
            final_price = base_price - discount_amount
            print(f"Product Name: {name}")
            print(f"Base Price: ${base_price:.2f}")
            print(f"Category: {category} (Discount: {category_discount}%)")
            print(f"Tier: {tier} (Discount: {tier_discount}%)")
            print(f"Total Discount Applied: {total_discount_percentage:.2f}%")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price after Discount: ${final_price:.2f}\n")
        print("Total Products statistics:\n")
        print(f"Total number of products: {total_products}")
        print(f"Average discount applied: {total_discount_applied/total_products:.2f}%")
    except FileNotFoundError:
        print(f"Error: The file was not found.")
