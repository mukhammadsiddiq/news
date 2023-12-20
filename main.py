import requests
from send_email import send_email

api_key = "51f34393d0ad42e4ae8b979f499a3cc3"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=51f34393d0ad42e4ae8b979f499a3cc3"
request = requests.get(url)
content = request.json()

message = ""
for article in content["articles"]:
    title = article.get("title", "")
    description = article.get("description", "")

    if title is not None and description is not None:
        message += title + "\n" + description + 2 * "\n"
message = message.encode("utf-8")
send_email(message)




