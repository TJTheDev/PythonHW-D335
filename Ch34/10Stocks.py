#TarrylonToneyStocks
"""

Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from the Old Town Stock Exchange, followed by an equivalent number of string inputs representing the stock selections. The following dictionary stock lists available stock selections as the key with the cost per selection as the value.
stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
Output the total cost of the purchased shares of stock to two decimal places.
The solution output should be in the format
Total price: $cost_of_stocks
 
Sample Input/Output:
If the input is
3
SOFI
AMZN
LVLU
then the expected output is
Total price: $150.53

"""

# Define the dictionary of stocks and their prices
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

# Get input for the number of stock selections
amountOfShares = int(input())  # Enter the number of stock selections

loopCheck = amountOfShares
finalCal = 0.00  # Variable to store the total cost of stocks
# sharePrice = 0.00  # Variable to store the price of each stock

# Iterate over the stock selections
while loopCheck > 0:
    try:
        # Get input for the stock choice as a string
        stockChoice = str(input()).strip  # Enter the stock symbol as a string

        # Calculate the total cost by adding the price of the selected stock to finalCal
        finalCal = finalCal + stocks[stockChoice]

        # Decrement the loop counter
        loopCheck = loopCheck - 1
    except:
        # Handle the exception if an invalid stock symbol is entered
        loopCheck = loopCheck - 1

# Print the total price of the stocks
print("Total price: $" + str(finalCal)) 
