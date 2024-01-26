import requests

from bs4 import BeautifulSoup

url = "https://skyranko.com/team/"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

all_title = (soup.find_all(class_="tp-team-v2-content"))

for element in all_title:
    e_name = element.find_all('h2')
    e_title = element.find_all('span')

    for h2 in e_name:
        print(f"\n{h2.get_text(strip=True)}")


    for span in e_title:
        print(f"{span.get_text(strip=True)}\n\n")