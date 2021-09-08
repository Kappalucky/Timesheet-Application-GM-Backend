"""Core Common: Functions for use throughout the application"""

# Python imports
import csv
import re
from datetime import datetime
from typing import Dict, Callable, Optional

# Django imports
from django.conf import settings

# 3rd party apps
# Local app imports
from .models import Timesheet


csv_path = '%s/GM_Coding_Exercise_Sample_Data.csv' % (settings.BASE_DIR)


def import_to_database():
    '''
    This function will create instances of the Timesheet model using data from a csv file every time it is called.
    It should only be called once or there will be duplicate data. Its purpose is solely to populate the database.
    '''

    # * Takes row information and display it as a dictionary per row
    reader = csv.DictReader(open(csv_path), delimiter=',')

    # * The row must follow the formatting or this function will fail
    for row in reader:

        billable = True if row['Billable?'] == 'Yes' else False
        date = datetime.strptime(row['Date'], '%m/%d/%y').date()

        timesheet = Timesheet(date=date,
                              client=row['Client'],
                              project=row['Project'],
                              project_code=row['Project Code'],
                              hours=row['Hours'],
                              billable=billable,
                              first_name=row['First Name'],
                              last_name=row['Last Name'],
                              billable_rate=row['Billable Rate'],
                              )

        timesheet.save()


def to_camel_case(snake_case_str: str) -> str:
    """
    Transforms snake_case to camelCase
    """
    components = snake_case_str.split('_')
    titled_components = ''.join(x.title() for x in components[1:])

    return f'{components[0]}{titled_components}'


def to_snake_case(camel_case_str: str) -> str:
    """
    Transforms camelCase to snake_case
    """

    return re.sub('([A-Z])([a-z0-9]+)', r'_\1\2', camel_case_str).lower()


def deep_case_transform(data: Dict, to_case_func: Callable) -> Optional[Dict]:
    transformed_data = {}

    if data is None:
        return

    if isinstance(data, list):
        new_data = []
        for obj in data:
            if isinstance(obj, dict):
                new_data.append(deep_case_transform(obj, to_case_func))
            else:
                new_data.append(obj)

        return new_data

    for key, value in data.items():
        transformed_key = to_case_func(key)
        if not isinstance(value, dict) and not isinstance(value, list):
            transformed_data[transformed_key] = value

        if isinstance(value, list):
            new_value = []
            for obj in value:
                if isinstance(obj, dict):
                    new_value.append(deep_case_transform(obj, to_case_func))
                else:
                    new_value.append(obj)

            transformed_data[transformed_key] = new_value

        if isinstance(value, dict):
            transformed_data[transformed_key] = deep_case_transform(
                value, to_case_func)

    return transformed_data


def deep_camel_case_transform(data: Dict) -> Dict:
    return deep_case_transform(data, to_camel_case)


def deep_snake_case_transform(data: Dict) -> Dict:
    return deep_case_transform(data, to_snake_case)
