import requests

from constants import json_url
from utils import MonthlyFile


def download_json_file():
    """
    :return: Extract a JSON file on the monthly basis.
    """
    print('-> Download started. . .')
    r = requests.get(json_url)
    extract_monthly_file = MonthlyFile()
    with open(extract_monthly_file.data, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print("-> Status code: ", r.status_code)
    print("-> Headers: ", r.headers['content-type'])
    print("-> Encoding: ", r.encoding)
    print("-> Download completed.")