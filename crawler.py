from bs4 import BeautifulSoup
import csv
import requests


# load website
url = "https://www.lix.polytechnique.fr/~hermann/conf.php"
res = requests.get(url)
doc = BeautifulSoup(res.text, "html.parser")
tables = doc.find_all('table')
# Write data to CSV file

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

        # for table in tables:
        #     a = ['table '+ str(table_count)] 
        #     writer.writerow(a)
        #     rows = table.find_all('tr')
        #     table_data = []
        #     for row in rows:
        #         cell_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
        #         table_data.append(cell_data)
        #     writer.writerows(table_data)
        #     table_count +=1
# business

# find table with conference class
tables = doc.find_all('table',class_="conference")

# take all the rows from tables
rows = tables.find_all('tr') 

for line in rows:
    cells = line.find_all('td')
    for cell in cells:
        print(cell.string)
        
roww = ""
