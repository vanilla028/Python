import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

key = []
value = []
dictionary = []



for element in soup.find('table').find_all('th'):
    key.append(element.text)

for element in soup.find('table').find('tbody').find_all('tr'):
    for td_element in element.find_all('td'):
        value.append(td_element.text)
    dictionary.append(dict(zip(key, value)))


print(key)
print(value)
print(dictionary)


