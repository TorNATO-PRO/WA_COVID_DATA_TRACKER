from datetime import datetime
from os import getcwd
from os import mkdir
from os import path

import requests


# Grabs the COVID-19 dataset from the Washington
# State Department of Health website
def download_file(url, file_format, directory):
    # tries to get the requested file, exits if unable to do so
    try:
        requested_file = requests.get(url)
    except requests.exceptions.Timeout:
        print('Connection Timeout!')
        return
    except requests.exceptions.TooManyRedirects:
        print('Too many redirects!')
        return
    except requests.exceptions.RequestException:
        print('Failed to connect to the server, check your internet connection!')
        return
    else:

        # verify that the file has been found at the given url
        if requested_file:
            print(f'Successfully found the file at the given url: {url}')
        else:
            print(f'An error has occurred while downloading the file, status code: {requested_file.status_code}')
            return

        current_time = datetime.now().strftime("%m-%d-%Y_%H_%M_%S")

        file_name = f'COVID-19_DATA_WASHINGTON_{current_time}.{file_format}'

        file_dir = create_directory(directory)

        file_name_with_directory = path.join(file_dir, file_name)

        # writes the dataset to a file with the following format
        # COVID-19_DATA_WASHINGTON_mm-dd-YYYY_hh_mm_ss
        open(file=file_name_with_directory, mode='wb').write(requested_file.content)

        print(f'Wrote the file: {file_name_with_directory}')

        return file_name_with_directory


# Creates a directory with a specified name
# in the current working directory
def create_directory(directory_name):
    # creates the directory at the current working directory
    corrected_directory_name = f'{getcwd()}/{directory_name}'
    if not path.isdir(corrected_directory_name):
        try:
            mkdir(corrected_directory_name)
        except OSError:
            print(f'Something went wrong! Unable to create directory {corrected_directory_name}')
            return
        else:
            print(f'Successfully created the directory {corrected_directory_name}')

    return corrected_directory_name
