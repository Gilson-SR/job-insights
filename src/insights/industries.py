from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, mode="r") as file:
        data_file = csv.DictReader(file)
        list_data_file = []
        for data in data_file:
            list_data_file.append(data)

    industries = set([industry['industry']
                      for industry in list_data_file
                      if industry['industry'] != ''])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industries = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_industries.append(job)
    return filtered_industries
