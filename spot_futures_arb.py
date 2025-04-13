def calculate_arbitrage():
    print("Arbitrage Calculator")
    print("-------------------\n")
    
    try:
        spot_price = float(input("Enter the spot price: "))
        futures_price = float(input("Enter the futures price: "))
        
        if spot_price <= 0:
            print("Error: Spot price must be greater than zero")
            return
        
        spread_pct = ((futures_price - spot_price) / spot_price) * 100
        
        print("\nResults:")
        print(f"Spot Price: ${spot_price:.4f}")
        print(f"Futures Price: ${futures_price:.4f}")
        print(f"Spread: {spread_pct:.2f}%")
        
        if spread_pct > 0:
            print("Direction: Buy Spot / Sell Futures")
            print(f"Potential Profit: {spread_pct:.2f}%")
        else:
            print("Direction: Sell Spot / Buy Futures")
            print(f"Potential Profit: {abs(spread_pct):.2f}%")
            
        print("\nNote: Remember to account for trading fees, funding rates, and slippage in actual trading.")
        
    except ValueError:
        print("Error: Please enter valid numerical values")

if __name__ == "__main__":
    while True:
        calculate_arbitrage()
        
        again = input("\nWould you like to calculate another? (y/n): ").lower()
        if again != 'y':
            break