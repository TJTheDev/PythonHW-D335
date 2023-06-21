#TarrylonToneyGrocery
"""
Create a solution that accepts a string input representing a grocery store item and an integer input identifying the number of items purchased on a recent visit. The following dictionary purchase lists available items as the key with the cost per item as the value.
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}
Additionally,
If fewer than ten items are purchased, the price is the full cost per item.
If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
If twenty-one or more items are purchased, the purchase gets a 10% discount.
Output the chosen item and total cost of the purchase to two decimal places.
The solution output should be in the format
item_purchased $total_purchase_cost
 
Sample Input/Output:
If the input is
bananas
12
then the expected output is
bananas $21.09
Alternatively, if the input is
cookies
144
then the expected output is
cookies $585.79

"""


# Define the dictionary of purchase items and their prices
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

# Get input for the item purchased
itemPurchased = str(input())  # Enter the name of the purchased item

# Get input for the quantity of the item purchased
purchaseQuantity = int(input())  # Enter the quantity of the purchased item

# Retrieve the price of the purchased item from the purchase dictionary
itemPrice = purchase[itemPurchased]  # Get the price of the purchased item
purchaseCal = purchase[itemPurchased]  # Variable to store the calculated price

itemDiscount = 0  # Variable to store the discount amount
totalPurchase = 0  # Variable to store the total purchase amount

# Calculate the total purchase amount based on the quantity and apply discounts if applicable
if purchaseQuantity <= 9:
    # No discount applied
    totalPurchase = purchaseCal * purchaseQuantity

elif purchaseQuantity >= 10 and purchaseQuantity <= 20:
    # Apply a 5% discount for quantities between 10 and 20
    itemDiscount = itemPrice * .05
    purchaseCal = itemPrice - itemDiscount
    totalPurchase = purchaseCal * purchaseQuantity
    totalPurchase = round(totalPurchase, 2)

else:
    # Apply a 10% discount for quantities greater than 20
    itemDiscount = itemPrice * .1
    purchaseCal = itemPrice - itemDiscount
    totalPurchase = purchaseCal * purchaseQuantity
    totalPurchase = round(totalPurchase, 2)

# Print the purchased item and the total purchase amount
print(itemPurchased, "$" + str(totalPurchase))
