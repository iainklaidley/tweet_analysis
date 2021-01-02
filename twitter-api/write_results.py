import os
import csv
from twitter_scrape_function import search_term

try: 
    os.mkdir(search_term)
except:
    print("Directory already exists.")
    pass

def write_results_to_csv(search_term, result):
    with open(search_term + '/results.csv', 'w') as csvfile:
        fieldnames = ['doc', 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in result.items():
            writer.writerow({'doc': k, 'label': v})