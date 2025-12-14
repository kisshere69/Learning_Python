import requests
import selectorlib
import smtplib, ssl


#Access the link as a legit user-agent
url = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#---Define functions---

def scrape(url):
    response = requests.get(url, HEADERS).text
    return response

def extract(response):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml").extract(response)["tours"]
    return extractor

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kizzfromdahood@gmail.com"
    password = "bikyrheswqbntxri"

    receiver = "app8flask@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email sent.")

def write(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted + "\n")

def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()

#---Call the functions---
scraped = scrape(url)
extracted = extract(scraped)
content = read(extracted)

#---Print out the result---
print(extracted)

#---Check if the extracted data is valid---
if extracted != "No upcoming tours":

    #---Check if data already exists. Send an email only if the data is new in the file--
    if extracted not in content:
        write(extracted)
        send_email(message = "New Event. Check it out!")