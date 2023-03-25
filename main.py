import requests
from send_the_mail import email
import random as rd

# Articles to Hand Over
# Title
# Description
# URL
# Author
# Content

# Articles to Hand Over (Apple)
# Title
# Author
# Description
# URL

api_key = "418b0abdbc8740fb80b9a96abb362e3f"
tesla_url = " \
https://newsapi.org/v2/everything?q=tesla&from=2023-02-25&sortBy=publishedAt&apiKey=418b0abdbc8740fb80b9a96abb362e3f&language=en"
tesla = requests.get(url=tesla_url)
tesla_news = tesla.json()

apple_url = '\
https://newsapi.org/v2/everything?q=apple&from=2023-03-24&to=2023-03-24&sortBy=popularity&apiKey=418b0abdbc8740fb80b9a96abb362e3f&language=en'
apple = requests.get(url=apple_url)
apple_news = apple.json()

business_url = "\
https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=418b0abdbc8740fb80b9a96abb362e3f&language=en"
business = requests.get(url=business_url)
business_news = business.json()

tech_crunch_url = "\
https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=418b0abdbc8740fb80b9a96abb362e3f&language=en"
tech_crunch = requests.get(url=tech_crunch_url)
tech_crunch_news = tech_crunch.json()

body = ''

for a_article in tesla_news['articles'][:10]:
    title = a_article['title']
    author = a_article['author']
    description = a_article['description']
    url = a_article['url']
    news_content = a_article['content']
    str1 = "News:"
    str2 = "Author:"
    str3 = "Description:"
    str4 = "URL:"

    if title and author and description and url and news_content is not None:
        body = f"Subject: Your Daily Tech News!" + "\n" + body + "\n" + str1 + " " + title + \
               "\n" + str2 + " " + author + "\n" + str3 + " " + description + "\n" + str4 + \
               " " + url + "\n" + "\n"

body2 = ''

for tc_news in apple_news['articles'][:10]:
    title2 = tc_news['title']
    author2 = tc_news['author']
    description2 = tc_news['description']
    url2 = tc_news['url']
    news_content2 = tc_news['content']
    str01 = "News:"
    str02 = "Author:"
    str03 = "Description:"
    str04 = "URL:"

    if title2 and author2 and description2 and url2 is not None:
        body2 = body2 + "\n" + str01 + " " + title2 + \
                "\n" + str02 + " " + author2 + "\n" + str03 + " " + description2 + "\n" + str04 + \
                " " + url2 + "\n" + "\n"

body3 = ''
for tc_news in business_news['articles'][:10]:
    title3 = tc_news['title']
    author3 = tc_news['author']
    description3 = tc_news['description']
    url3 = tc_news['url']
    news_content3 = tc_news['content']
    str11 = "News:"
    str22 = "Author:"
    str33 = "Description:"
    str44 = "URL:"

    if title3 and author3 and description3 and url3 is not None:
        body3 = body3 + "\n" + str11 + " " + title3 + \
                "\n" + str22 + " " + author3 + "\n" + str33 + " " + description3 + "\n" + str44 + \
                " " + url3 + "\n" + "\n"

body4 = ''
subject = "Your Daily Business News!"
for tc_news in tech_crunch_news['articles'][:10]:
    title4 = tc_news['title']
    author4 = tc_news['author']
    description4 = tc_news['description']
    url4 = tc_news['url']
    news_content4 = tc_news['content']
    strn1 = "News:"
    strn2 = "Author:"
    strn3 = "Description:"
    strn4 = "URL:"
    if title4 and author4 and description4 and url4 is not None:
        body4 = f"Subject: Your Daily Business News" + "\n" + body4 + "\n" + strn1 + " " + title4 + \
                "\n" + strn2 + " " + author4 + "\n" + strn3 + " " + description4 + "\n" + strn4 + \
                " " + url4 + "\n" + "\n"

body = body.encode("utf-8")
body2 = body2.encode("utf-8")
body3 = body3.encode("utf-8")
body4 = body4.encode("utf-8")

real_body = body + body2 + body3
email(real_body)
email(body4)












