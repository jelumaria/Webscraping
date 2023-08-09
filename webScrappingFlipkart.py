import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/tablets/pr?sid=hry&p%5B%5D=facets.price_range.from%3D15000&p%5B%5D=facets.price_range.to%3D20000&otracker=clp_creative_card_3_34.creativeCard.CREATIVE_CARD_tablets-store_JX5XR7FSGB76&fm=neo%2Fmerchandising&iid=M_c115c574-c73c-42cd-9b4f-42aa2313479c_34.JX5XR7FSGB76&ppt=clp&ppn=tablets-store&ssid=t22oxa3z3k0000001691588580738'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")  # Using "html.parser" instead of "lxml"

names = soup.find_all("a", class_="s1Q9rs")
prices = soup.find_all("div", class_="_30jeq3")

# Create a CSV file and write the data into it
with open('tablet_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])  # Write header

    for name, price in zip(names, prices):
        name_text = name.text.strip()
        price_text = price.text.strip()

        writer.writerow([name_text, price_text])

print("Data scraped and saved to tablet_data.csv")
