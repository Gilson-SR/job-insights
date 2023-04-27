from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r") as file:
        data_file = csv.DictReader(file)
        list_data_file = []
        for data in data_file:
            list_data_file.append(data)
        return list_data_file


def get_unique_job_types(path: str) -> List[str]:
    data_jobs = read(path)
    job_types = set()
    for job in data_jobs:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
