import requests

GIPHY_API_KEY = ""  

def fetch_gif_url(query: str) -> str:
    try:
        response = requests.get(
            "https://api.giphy.com/v1/gifs/search",
            params={"q": query, "api_key": GIPHY_API_KEY, "limit": 1}
        )
        data = response.json()
        if data["data"]:
            return data["data"][0]["images"]["downsized"]["url"]
    except Exception as e:
        print(f"Error fetching GIF for {query}: {e}")
    return ""
