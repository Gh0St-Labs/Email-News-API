import requests
from send_the_mail import email
import random as rd

# Articles to Hand Over
# Title
# Description
# URL
# Author
# Content

news_topics = 'tesla'

api_key = "418b0abdbc8740fb80b9a96abb362e3f"
url = "https://newsapi.org/v2/everything?" \
      f"q={news_topics}&from=2023-02-23&sortBy=publishedAt&api" \
      "Key=418b0abdbc8740fb80b9a96abb362e3f&language=en"

random_subjects = ["Today's News!", "Breaking News!", "News Has Arrived!", "Daily News Has Arrived",
                   "Today's News Highlights!", "Shattering News Highlights!", "Today's Highlights!"]
choose_subjects = rd.choice(random_subjects)

read_the_requests = requests.get(url=url)
contents = read_the_requests.json()

title = ""
author = ""
description = ""
url = ""
news_content = ""
body = ""

for one_artice in contents['articles'][:20]:
      title = one_artice['title']
      author = one_artice['author']
      description = one_artice['description']
      url = one_artice['url']
      news_content = one_artice['content']
      str1 = "News:"
      str2 = "Author:"
      str3 = "Description:"
      str4 = "URL:"
      if title and author and description and url and news_content is not None:
            body = f"Subject: {choose_subjects}" + "\n" + body + "\n" + str1 + " " + title + \
                   "\n" + str2 + " " + author + "\n" + str3 + " " + description + "\n" + str4 + \
                   " " + url + "\n" + "\n"



body = body.encode("utf-8")
email(body)


