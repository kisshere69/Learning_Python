import requests
import selectorlib
from datetime import datetime

#Access the link as a legit user-agent
url = "https://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#---Define functions---

def scrape(url):
    response = requests.get(url, HEADERS).text
    return response

def extract(response):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml").extract(response)["home"]
    return extractor

def write(extracted):
    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    with open("data.txt", "a") as file:
        line = f"{now} {extracted}\n"
        file.write(line)

#---Call the functions---

scraped = scrape(url)
extracted = extract(scraped)
write(extracted)