from datetime import datetime

import data_grabber as dg


# Grabs WA COVID-19 data from the internet
def grab_internet_covid_data():
    covid19_wa_url = 'https://www.doh.wa.gov/Portals/1/Documents/1600/coronavirus' \
                     '/data-tables/WA_COVID19_Cases_Hospitalizations_Deaths.xlsx'

    file_format = 'xlsx'
    current_time = datetime.now().strftime("%m-%d-%Y_%H_%M_%S")

    file_name = f'COVID-19_DATA_WASHINGTON_{current_time}.{file_format}'

    return dg.download_file(url=covid19_wa_url, directory='Downloads', name=file_name)


# My main method
def main():
    dataset = grab_internet_covid_data()


# Calls the main method :)
if __name__ == '__main__':
    main()
