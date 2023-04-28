from typing import Union, List, Dict
import csv


def get_max_salary(path: str) -> int:
    with open(path, mode="r") as file:
        data_file = csv.DictReader(file)
        list_data_file = []
        for data in data_file:
            list_data_file.append(data)

    salaries = []
    for salary in list_data_file:
        if salary["max_salary"] != "" and salary["max_salary"] != "invalid":
            salaries.append(int(salary["max_salary"]))
    return max(salaries)


def get_min_salary(path: str) -> int:
    with open(path, mode="r") as file:
        data_file = csv.DictReader(file)
        list_data_file = []
        for data in data_file:
            list_data_file.append(data)

    salaries = []
    for salary in list_data_file:
        if salary["min_salary"] != "" and salary["min_salary"] != "invalid":
            salaries.append(int(salary["min_salary"]))
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
        if min_salary > max_salary:
            raise ValueError
        return min_salary <= salary <= max_salary
    except (ValueError, TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
