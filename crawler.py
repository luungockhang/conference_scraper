from bs4 import BeautifulSoup
import requests

# load website
url = "https://www.lix.polytechnique.fr/~hermann/conf.php"

res = requests.get(url)
doc = BeautifulSoup(res.text, "html.parser")


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