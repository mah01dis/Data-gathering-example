from google_play_scraper import search

def search_apps(query, num_results=10):
    query = f"hyper-casual {query}" 
    results = search(
        query,
        n_hits=num_results,
        lang="en",  # Language (defaults to 'en')
        country="us"  # Country code (defaults to 'us')
    )

    for i, app in enumerate(results):
        print(f"Result {i + 1}:")
        print(f"Title: {app['title']}")
        print(f"App ID: {app['appId']}")
     #   print(f"URL: {app['url']}")
     #   print(f"Developer: {app['developer']}")
      #  print(f"Icon URL: {app['icon']}")
      #  print(f"Description: {app['summary']}\n")

if __name__ == '__main__':
    search_apps("games", num_results=10)