import requests
from bs4 import BeautifulSoup
 
# response = requests.get("https://www.google.com")
# # print(.text)

# soup = BeautifulSoup(response.text, 'html.parser')
# # print(soup.prettify())

# for heading in soup.find_all("p"):
#   print(heading.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'Vaibhav',
    "body": 'bhai',
    "userId": 12,
  }
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
  }
response = requests.post(url, headers=headers, json=data)

print(response.text)