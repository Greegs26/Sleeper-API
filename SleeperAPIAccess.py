import pandas as pd

# Define the Sleeper API endpoint for all player data
SLEEPER_API_URL = "https://api.sleeper.app/v1/players/nfl"

# Read the JSON data directly into a pandas DataFrame
player_data = pd.read_json(SLEEPER_API_URL)

# Display the first few rows of the DataFrame
print(player_data.head())

# Save the player data to a CSV file if needed
player_data.to_csv('sleeper_player_data.csv', index=False)

print("Player data successfully downloaded and saved to 'sleeper_player_data.csv'.")