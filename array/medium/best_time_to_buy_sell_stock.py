prices=[7,1,5,1,6,4]
left = 0 #Buy
right = 1 #Sell
max_profit = 0
while right < len(prices):
    currentProfit = prices[right] - prices[left] #our current Profit
    if prices[left] < prices[right]:
        max_profit =max(currentProfit,max_profit)
    else:
        left = right
    right += 1
print(max_profit)


#firstly we are checking if the right value that is sell value if is less to the buy value  
#that is right that is 7>1 in that case we increment left to position of 1 
#next we check from 1 to len() so as to find max profit
