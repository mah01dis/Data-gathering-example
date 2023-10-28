import requests
import json

# Define the URL for scraping top games from the Google Play Store
url = "https://serpapi.com/search?engine=google_play"
# Set your API key here
api_key = "your API key"

# Define the parameters for the request
params = {
    "list_name": "topselling_free",
    "cat_key": "GAME",
    "country": "US",
    "limit": 10,  # Number of games to fetch
    "access_token": api_key,
}

# Send an HTTP GET request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    top_games = data.get("list")

    if top_games:
        print("Top 10 Games in the Google Play Store:")
        for i, game in enumerate(top_games):
            print(f"{i + 1}. {game['title']}")
    else:
        print("No data found.")
else:
    print("Failed to fetch data. Status code:", response.status_code)
