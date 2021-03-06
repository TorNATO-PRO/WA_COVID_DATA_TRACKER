import data_grabber as dg


# Grabs WA COVID-19 data from the internet
def grab_internet_covid_data():
    covid19_wa_url = 'https://www.doh.wa.gov/Portals/1/Documents/1600/coronavirus' \
                     '/data-tables/WA_COVID19_Cases_Hospitalizations_Deaths.xlsx'

    dataset = dg.download_file(url=covid19_wa_url, file_format="xlsx", directory="Downloads")


# My main method
def main():
    grab_internet_covid_data()


# Calls the main method :)
if __name__ == '__main__':
    main()
