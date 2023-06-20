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

stocks = {'TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

amountOfShares = int(input())
loopCheck = amountOfShares
finalCal = 0.00
sharePrice = 0.00

while loopCheck > 0:
#    stockChoice = str(input())
#   I switched this to a try block to handle input validation better
    try:
        stockChoice = str(input())
        finalCal = round(finalCal + stocks[stockChoice],2) 
#       stockChoice = "'"+stockChoice+"'"
#       print(stockChoice)
#       print (stocks[stockChoice])
#       finalCal = finalCal + int(stocks[stockChoice])
#       sharePrice = int(stocks[stockChoice])
#       round(finalCal = finalCal + stocks[stockChoice],2)
        loopCheck = loopCheck - 1
    except:
        loopCheck = loopCheck - 1
    
print("Total price:" + ": $", finalCal)
