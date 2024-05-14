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
                cell_with_confname = row.find_all("td",class_="confname")
                # [<td class="confname"><a href="https://www.iclp24.utdallas.edu/" target="_blank">ICLP<br>&nbsp;</a>
                #   <span class="tooltiptext">International Conference on Logic Programming</span>
                # </td>]
                if len(cell_with_confname) != 0: 
                    a_tag = cell_with_confname[0].find_all("a",href=True) 
                    # [<a href="https://www.iclp24.utdallas.edu/" target="_blank">ICLP<br>&nbsp;</a>]
                    website_link = a_tag[0]['href']
                    cell_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    cell_data.append(website_link)
                    table_data.append(cell_data)
                else:
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