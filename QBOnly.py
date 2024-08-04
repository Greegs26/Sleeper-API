import pandas as pd

# Define the Sleeper API endpoint for all player data
SLEEPER_API_URL = "https://api.sleeper.app/v1/players/nfl"

# Read the JSON data directly into a pandas DataFrame
player_data = pd.read_json(SLEEPER_API_URL)

# Filter the DataFrame to include only QBs
qbs = player_data[player_data['position'] == 'QB']

# Display the first few rows of the filtered DataFrame
print(qbs.head())

# Save the QB data to a CSV file
qbs.to_csv('sleeper_qb_data.csv', index=False)

print("QB data successfully downloaded and saved to 'sleeper_qb_data.csv'.")