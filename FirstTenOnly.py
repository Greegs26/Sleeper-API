import pandas as pd

# Define the Sleeper API endpoint for all player data
SLEEPER_API_URL = "https://api.sleeper.app/v1/players/nfl"

# Read the JSON data directly into a pandas DataFrame
player_data = pd.read_json(SLEEPER_API_URL)

# Select the first 10 players
first_10_players = player_data.head(10)

# Display the first 10 rows of the DataFrame
print(first_10_players)

# Save the first 10 players data to a CSV file
first_10_players.to_csv('sleeper_first_10_players.csv', index=False)

print("First 10 player data successfully downloaded and saved to 'sleeper_first_10_players.csv'.")