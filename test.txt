import requests
from bs4 import BeautifulSoup
import yaml

def grab_api():
    url = "https://ccfddl.github.io/conference/allconf.yml"
    res = requests.get(url)
    # Retrieve the file content from the URL
    response = requests.get(url, allow_redirects=True)
    # Convert bytes to string
    content = response.content.decode("utf-8")
    # Load the yaml
    content = yaml.safe_load(content)
    
    for conference_org in content:
        
    print(content)
    
    
    
grab_api()
