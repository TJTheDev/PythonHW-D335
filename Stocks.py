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

sharePurchase = int(input())

portfolio = sharePurchase / stocks[sharePurchase]



print("Total price:" + ": $", portfolio)