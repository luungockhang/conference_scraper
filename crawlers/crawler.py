# Created by 22880068, 22880179
# May 15 2024
# v0.1
# To crawl lix.polytechnique.fr

from bs4 import BeautifulSoup
import csv
import requests
import time
import random
import os
import re

def crawler():
    # load website
    url = "https://www.lix.polytechnique.fr/~hermann/conf.php"
    res = requests.get(url)
    doc = BeautifulSoup(res.text, "html.parser")
    tables = doc.find_all('table')
    
    # data goes to this folder
    file_number = 1
    folder = 'conference_list_site/lix.polytechnique.fr'
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_name = 'output' + str(file_number) + '.csv'
    file_path = os.path.join(folder,file_name)
    
    # Write data to CSV. Each table = 1  CSV.
    for table in tables:
        with open(file_path, 'w',encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            rows = table.find_all('tr')
            table_data = []
            for row in rows:
                cell_with_confname = row.find_all("td",class_="confname")
                # [<td class="confname"><a href="https://www.iclp24.utdallas.edu/" target="_blank">ICLP<br>&nbsp;</a>
                #   <span class="tooltiptext">International Conference on Logic Programming</span>
                # </td>]
                if len(cell_with_confname) != 0: # If it is not header row
                    a_tag = cell_with_confname[0].find_all("a",href=True) 
                    # [<a href="https://www.iclp24.utdallas.edu/" target="_blank">ICLP<br>&nbsp;</a>]
                    website_link = a_tag[0]['href']
                    cell_data = []
                    conf_full_name = ''
                    conf_short_name = ''
                    year = ''
                    for cell in row.find_all(['th','td']): # get all cells in a row
                        if cell['class'][0] == 'date':
                            date = cell.get_text()
                            if len(date) > 0:
                                match = re.search(r"\d{4}", date)
                                year = match.group()
                            else:
                                year = ''
                        if cell['class'][0] == 'confname': # if this class is confname
                            conf_short_name = cell.a.get_text()
                            conf_full_name = cell.span.get_text()
                            cell_data.append(conf_short_name)
                            continue
                        cell_data.append(cell.get_text(strip=True))
                    if not year == '':
                        cell_data[0]+= " {0}".format(year)
                    cell_data.append(website_link)
                    cell_data.append(conf_full_name)
                    table_data.append(cell_data)
                else:
                    cell_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    cell_data.append('Website')
                    cell_data.append('Description')
                    table_data.append(cell_data)
            del table_data[-1] # Delete the final row (which is another header)
            writer.writerows(table_data)
            file_number+=1
            file_name = 'output' + str(file_number) + '.csv'
            file_path = os.path.join(folder,file_name)
            
while True:
    crawler()
    interval = random.randrange(5,10)
    
    print("crawled. next at {0}".format(interval))
    time.sleep(interval)