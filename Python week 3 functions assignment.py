def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price
    
price = float(input("Enter the original price:"))
discount_percent = float(input("Enter percentage discount:"))
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")