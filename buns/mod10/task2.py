import requests
import re

url = 'http://www.columbia.edu/~fdc/sample.html'
site = input("Введите URL ")
correct = re.search(r'https?://[^/]+/?.*?$', site)

if correct:
    site_request = str(requests.get(site))
    if re.search(r'200', site_request):
        url = site
    else:
        print("Код ответа не 200, будет использован URL из примера")
else:
    print("Некорректный ввод, будет использован URL из примера")

response = requests.get(url)
html_data = response.text
h3_parsed = re.findall(r'<h3.*?>(.*?)<\/h3>', html_data)
if len(h3_parsed) == 0:
    print("h3 теги не найдены")
else:
    print(h3_parsed)
    for item in h3_parsed:
        print(item)
