import requests
# Articles to Hand Over
# Title
# Description
# URL
# Author
# Content

api_key = "418b0abdbc8740fb80b9a96abb362e3f"
url = "https://newsapi.org/v2/everything?" \
      "q=tesla&from=2023-02-23&sortBy=publishedAt&api" \
      "Key=418b0abdbc8740fb80b9a96abb362e3f"


read_the_requests = requests.get(url=url)
content = read_the_requests.json()

print(content['articles'])
