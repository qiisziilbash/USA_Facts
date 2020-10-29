from utils.plots import *
from utils.data_reader import *

if __name__ == "__main__":

    counties_file_address = 'data/raw/counties.json'
    data_file_address = 'data/raw/poverty_by_state.xlsx'

    data, counties = read_poverty_data(data_file_address)

    data, dates = clean_covid_data(data)

    data = reduce_data_columns(data, dates, ['countyFIPS'])

    for date in dates:
        print('>>> Date: ' + date)
        plot_a_day(data[['countyFIPS', date]], counties, date, show=False, save=True)

    # animate_over_time(covid_data, counties_data, dates[0:6])
