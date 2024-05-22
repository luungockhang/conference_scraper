# Created by 22880068, 22880179
# May 15 2024
# v0.1
# To crawl ccfddl.github.io

import csv
import requests
import time
import random
import os
import yaml

def crawl_api():
    url = "https://ccfddl.github.io/conference/allconf.yml"
    # Retrieve the file content from the URL
    response = requests.get(url, allow_redirects=True)
    # Convert bytes to string
    content = response.content.decode("utf-8")
    # Load the yaml
    content = yaml.safe_load(content)
    
    # data goes to this folder
    folder = 'conference_list_site/ccfddl.github.io'
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_name = 'output.csv'
    file_path = os.path.join(folder,file_name)
    
    # write data
    with open(file_path,'w',encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        table_data = []
        table_data.append(['Conference', 'City, Country', 'Deadline', 'Date', 'Website','Description'])
        for conference_org in content:
            title = conference_org['title']
            description = conference_org['description']
            for confs in conference_org['confs']:
                cell_data = []
                cell_data.append(str(title + " " + str(confs['year'])))
                cell_data.append(confs['place'])
                timeline_str = ''
                for timeline in confs['timeline']:
                    timeline_str +='Deadline: {0}\n'.format(timeline['deadline'])
                    if 'abstract_timeline' in timeline.keys():
                        timeline_str += 'Abstract timeline: {0}\n'.format(timeline['abstract_timeline'])
                    if 'comment' in timeline.keys():
                        timeline_str += 'Comment: {0}\n'.format(timeline['comment'])
                cell_data.append(timeline_str)
                cell_data.append(confs['date'])
                cell_data.append(confs['link'])
                cell_data.append(description)
                table_data.append(cell_data)
        writer.writerows(table_data)
        
async def run():
    crawl_api()
    print('ccfddl.github.io crawled')