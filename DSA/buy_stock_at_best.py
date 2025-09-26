# Given a list stock prices, find best price to buy and sell stock
# to maximize profit. You must buy before you sell.

def find_max_profit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
            
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit
            
        sell_price = min_price + max_profit
        
    return min_price, sell_price, max_profit

if __name__ == "__main__":
    stock_prices = [7, 1, 5, 3, 6, 4]
    min_price, sell_price, max_profit = find_max_profit(stock_prices)
    print(f"Buy at: {min_price}, Sell at: {sell_price}, Max Profit: {max_profit}")