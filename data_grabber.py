from os import getcwd
from os import mkdir
from os import path

import requests


# Downloads a file from a url, saves it in
# a specified directory within the working
# directory with a given name
def download_file(url, directory, name):
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

        file_dir = create_directory(directory)

        file_name_with_directory = path.join(file_dir, name)

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
