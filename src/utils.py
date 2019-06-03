import os

from constants import path_us, file_name


class MonthlyFile:
    root = os.path.dirname(__file__)
    path = path_us
    file_name = file_name
    data = os.path.join(root, path, file_name)
