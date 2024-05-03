from bs4 import BeautifulSoup
import csv
import requests

# load website
url = "https://www.lix.polytechnique.fr/~hermann/conf.php"
res = requests.get(url)
doc = BeautifulSoup(res.text, "html.parser")
tables = doc.find_all('table')
# Write data to CSV file
with open('output.csv', 'w',encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    table_count = 1
    for table in tables:
        a = ['table '+ str(table_count)] 
        writer.writerow(a)
        rows = table.find_all('tr')
        table_data = []
        for row in rows:
            cell_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
            table_data.append(cell_data)
        writer.writerows(table_data)
        table_count +=1
        for line in rows:
    cells = line.find_all('td')
    for cell in cells:
        print(cell.string)