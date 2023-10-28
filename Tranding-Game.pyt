import os
import google_auth_oauthlib.flow
import googleapiclient.discovery

# Set the API key you obtained from the Google Developers Console
api_key = "your API key"

# Set up the YouTube Data API client
def get_youtube_trending_games(api_key):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)

    # Define the parameters for the search
    request = youtube.videos().list(
        chart="mostPopular",
        regionCode="US",  # You can change the region code as needed
        videoCategoryId="20",  # 20 corresponds to "Gaming" category
        part="snippet"  # Specify that you want snippet information
    )

    response = request.execute()

    for video in response["items"]:
     print("Video Title:", video["snippet"]["title"])
     print("Video ID:", video["id"])
     print("Video Description:", video["snippet"]["description"])
     print("\n")

if __name__ == "__main__":
    get_youtube_trending_games(api_key)