import requests

api_key = "f8b70a5ba81848a6a8e4c19f07e0810b"
url = ("https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&"
       "apiKey=f8b70a5ba81848a6a8e4c19f07e0810b")

# Make a request
req = requests.get(url)

# Get a dictionary with data
content = req.json()

# Access the article titles
for article in content['articles']:
       print(article["title"])