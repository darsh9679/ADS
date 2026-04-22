import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA 
# Sample Time Series Data (e.g., daily sales) 
data = [10, 12, 13, 15, 18, 20, 22, 25, 28, 30] 
df = pd.Series(data) 
# Fit ARIMA Model (p, d, q parameters) 
# (1, 1, 1) is a common starting point for simple trends 
model = ARIMA(df, order=(1, 1, 1)).fit() 
# Forecast next 3 steps 
forecast = model.forecast(steps=3) 
print("Historical Data:", data) 
print("Forecasted Values:", forecast.tolist())