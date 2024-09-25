def calculate_discount(total_purchase):
    if total_purchase > 5000:
        discount = total_purchase * 0.10
    else:
        discount = total_purchase * 0.05
    final_price = total_purchase - discount
    return discount, final_price

while True:
    total_purchase = float(input("Enter the total purchase amount: "))
    
    discount, final_price = calculate_discount(total_purchase)
    
    print(f"Initial Purchase Amount: {total_purchase:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")
    
    option = input("Do you want to try again? (yes/no): ").lower()
    if option != 'yes':
        break
print("Thank you!")
        
