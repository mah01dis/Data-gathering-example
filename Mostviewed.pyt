import googleapiclient.discovery

# Set your API key here
API_KEY = 'AIzaSyCViakDt1TE7RNr8svnAD2MN7NvybyKsMw'

# Create a YouTube Data API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

def get_most_viewed_video():
    try:
        # Request the most viewed videos from the YouTube API
        request = youtube.videos().list(
            part="snippet,statistics",
            chart="mostPopular",
            regionCode="US",  # You can change the region code if needed
        )
        response = request.execute()

        # Extract the most viewed video from the response
        most_viewed_video = response['items'][0]
        video_id = most_viewed_video['id']
        title = most_viewed_video['snippet']['title']
        view_count = most_viewed_video['statistics']['viewCount']

        print(f"Most Viewed Video: {title}")
        print(f"Video ID: {video_id}")
        print(f"View Count: {view_count}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    get_most_viewed_video()
