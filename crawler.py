# Deprecated. Crawlers are stored in "crawlers" folder.

from bs4 import BeautifulSoup
import csv
import requests
import time
import random

def crawler():
    # load website
    url = "https://www.lix.polytechnique.fr/~hermann/conf.php"
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")
    tables = doc.find_all('table')
    
    # Write data to CSV. Each table = 1  CSV.
    file_number = 1
    file_name = 'output' + str(file_number) + '.csv' 
    for table in tables:
        with open(file_name, 'w',encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            rows = table.find_all('tr')
            table_data = []
            for row in rows:
                cell_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                table_data.append(cell_data)
            writer.writerows(table_data)
            file_number+=1
            file_name = 'output' + str(file_number) + '.csv'
            
while True:
    crawler()
    interval = random.randrange(5,10)
    
    print("crawled. next at {0}".format(interval))
    time.sleep(interval)