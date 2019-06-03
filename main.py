from extract_json_data import download_json_file
from get_file_vanilla import read_file
from utils import MonthlyFile


def main():
    """

    :return:
    """
    download_json_file()
    process = MonthlyFile()
    read_file(process.data)


if __name__ == '__main__':
    main()
