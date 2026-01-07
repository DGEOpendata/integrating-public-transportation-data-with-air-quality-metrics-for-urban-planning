python
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the transportation dataset
transport_data = pd.read_csv('Public_Transportation_Usage.csv')

# Load the air quality dataset
with open('Air_Quality_Data.json') as f:
    air_quality_data = json.load(f)

# Convert air quality data to DataFrame
air_quality_df = pd.json_normalize(air_quality_data)

# Merge datasets on the 'date' column
merged_data = pd.merge(transport_data, air_quality_df, on='date')

# Analyze peak transportation usage and corresponding air quality
# Filter for peak usage times
peak_usage = merged_data[merged_data['passenger_count'] > merged_data['passenger_count'].quantile(0.75)]

# Plotting
plt.figure(figsize=(14, 7))
plt.scatter(peak_usage['passenger_count'], peak_usage['PM2.5'], c='red', label='PM2.5')
plt.scatter(peak_usage['passenger_count'], peak_usage['NO2'], c='blue', label='NO2')
plt.title('Peak Transportation Usage vs Air Quality')
plt.xlabel('Passenger Count')
plt.ylabel('Pollutant Levels')
plt.legend()
plt.show()

# Conclusion: Identify correlations between high passenger count and pollutant levels
print("Correlation analysis:")
print(peak_usage[['passenger_count', 'PM2.5', 'NO2']].corr())

