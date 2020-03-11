
# Standard library imports
import os

# Third party imports (dependencies)
import xlwings as xw
import pandas as pd
import matplotlib.pyplot as plt


@xw.sub  # only required if you want to import it or run it via UDF Server
def main():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


# UDF function that was generated here has been deleted (not used)


# -----------------------------------------------------------------------------
# EXERCISE 3
# ----------
def create_daterange_dataframe(filename, start_date, end_date):
    '''Helper function'''

    # Get the 'correct' current working dir (where the .py and .xlsm files are)
    cwd = os.path.dirname(os.path.abspath(__file__))

    # Combine into a full path to the dataset file
    full_filename = f'{cwd}\\{filename}'

    df_raw = pd.read_csv(full_filename)

    # Change the "raw" dates into datetime objects so they can be filtered
    df_raw['Date'] = pd.to_datetime(df_raw['Date'])

    # Set the date as the index of the dataframe
    df = df_raw.set_index('Date')

    # Filter dataframe for input date range and return it
    return df[start_date:end_date]


@xw.sub
def update_weather_plot():
    '''Macro function to interact with Excel'''

    # Mock the calling Excel file
    xw.books.active.set_mock_caller()

    # Get the workbook that is calling the macro and set sheet
    wb = xw.Book.caller()
    sht3 = wb.sheets['Sheet3']

    # Get input values from Excel
    start_date = sht3.range('C21').value
    end_date = sht3.range('C22').value
    parameter = sht3.range('C23').value

    fig, ax = plt.subplots()

    filename = 'Sydney_weather.csv'

    # Create a dataframe from the dataset and filter it based on inputs
    df = create_daterange_dataframe(filename, start_date, end_date)

    # Use the Pandas interface to matplotlib for plotting
    df.plot(y=parameter, ax=ax)

    # Insert figure into sheet
    sht3.pictures.add(fig, name='MyPlot', update=True)

# -----------------------------------------------------------------------------


if __name__ == "__main__":
    xw.books.active.set_mock_caller()
    main()

    # -------------------------------------------------------------------------
    # EXERCISE 2
    # ----------
    import numpy as np

    # Establish connection to the workbook
    wb = xw.Book.caller()

    sht2 = wb.sheets['Sheet2']

    sht2.range('A2').options(transpose=True).value = np.arange(-50, 51, 5)

    # -------------------------------------------------------------------------
