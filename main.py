# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the function to calculate the moving average
def calculate_moving_average(data, period):
    """Calculate the moving average of a data series."""

    # Calculate the moving average
    moving_average = data.rolling(window=period).mean()

    # Return the moving average
    return moving_average

# Load the data from a CSV file
data = pd.read_csv('data.csv')

# Calculate the 20-period exponential moving average (EMA)
ema_20 = data['Close'].ewm(span=20, adjust=False).mean()

# Plot the data and the EMA
plt.plot(data['Close'], label='Close Price')
plt.plot(ema_20, label='20-period EMA')
plt.legend()
plt.show()

# Get the current price from the last row of the data
current_price = data['Close'].iloc[-1]

# Define the stop loss percentage
stop_loss_percentage = 0.05

# Define the take profit percentage
take_profit_percentage = 0.10

# Calculate the stop loss price
stop_loss_price = current_price * (1 - stop_loss_percentage)

# Calculate the take profit price
take_profit_price = current_price * (1 + take_profit_percentage)

# Print the stop loss and take profit prices
print("Stop Loss Price:", stop_loss_price)
print("Take Profit Price:", take_profit_price)

# Compare the current price with the EMA to determine the buy/sell signal
if current_price > ema_20.iloc[-1]:
    print("Buy Signal")
elif current_price < ema_20.iloc[-1]:
    print("Sell Signal")
else:
    print("Hold Signal")