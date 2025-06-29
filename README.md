# Arbitrage Calculator

## Overview

This Arbitrage Calculator is a Python tool designed to help traders identify potential arbitrage opportunities between spot and futures markets. The tool calculates the percentage spread between manually entered spot and futures prices, determines the optimal arbitrage direction, and estimates potential profit percentages.

## Features

- **Simple Input**: Users manually enter spot and futures prices for quick calculations
- **Spread Calculation**: Computes the percentage difference between spot and futures prices
- **Direction Guidance**: Recommends whether to buy spot/sell futures or vice versa
- **Profit Estimation**: Provides potential profit percentage based on the spread
- **User-Friendly**: Interactive command-line interface with clear output

## Usage

1. Run the script in a Python environment (Python 3.6+ recommended)
2. Follow the prompts to enter:
   - Spot price of the asset
   - Futures price of the same asset
3. The calculator will display:
   - The calculated spread percentage
   - Recommended arbitrage direction
   - Potential profit estimate

## Important Notes

- This calculator provides theoretical values only
- Real-world trading requires consideration of:
  - Trading fees
  - Funding rates (for perpetual futures)
  - Slippage
  - Liquidity constraints
  - Withdrawal/deposit limits
- The calculator assumes prices are for the same asset on comparable markets

## Requirements

- Python 3.x
- No external dependencies required

## Example Output

```
Arbitrage Calculator
-------------------

Enter the spot price: 50000
Enter the futures price: 50250

Results:
Spot Price: $50000.0000
Futures Price: $50250.0000
Spread: 0.50%
Direction: Buy Spot / Sell Futures
Potential Profit: 0.50%

Note: Remember to account for trading fees, funding rates, and slippage in actual trading or chech the helper
https://github.com/Cathitler/Spot-futures-abitarage.-cash-and-carry-calculator/blob/main/Helper
```

## Disclaimer

This tool is for educational purposes only. Cryptocurrency trading involves substantial risk of loss and is not suitable for every investor. Past performance is not indicative of future results. Always conduct your own research before making any trading decisions.
