import requests

# Replace 'YOUR_API_KEY' with your News API key
api_key = 'YOUR_API_KEY'

# Define the URL to the News API endpoint for US news
url = f'https://content.guardianapis.com/search?api-key=94ef0e7b-774f-4235-b792-2046a375a549'

# Send an HTTP GET request to fetch the news data
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for article in data['response']['results']:
         if(data['response']['results'][0]['sectionId'] != 'politics'):
          print(data['response']['results'][0]['id'])

          
     # Extract and print the titles and descriptions of news articles
    for article in data['articles']:
        title = article['title']
        description = article['description']

        print("Title:", title)
        print("Description:", description)

        # Use Gensim to summarize the description
        summary = summary(description, ratio=0.2)

        print("Summary:", summary)
        print("\n")
else:
    print("Failed to fetch news data. Status code:", response.status_code)
