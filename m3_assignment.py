#Question 1
#create a function

#def calculate_discount(price, discount_percent):
#    if discount_percent >= 20:
#        price = price * discount_percent / 100
#        print(f"price: {price}")
#    else:
#        print("discount is less than 20%")

#calculate_discount(2000, 25)

#Qestion 2
#prompt user to enter value for price and discount on product
def calculate_discount():
    price = int(input("Enter price of product: "))
    discount_percent = input("Enter discount on product: ")
    if discount_percent.strip() == "":
        print("No discount was entered for this product.")
        return  # stop here since there's no discount
    else:
        discount_percent = int(discount_percent)
    if discount_percent == 0:
        print("There is no discount for this product. ")
    elif discount_percent >= 20:
        price = price - (price * discount_percent / 100)
        print(f"price: {price}")
    else:
        print("discount is less than 20%")

calculate_discount()
