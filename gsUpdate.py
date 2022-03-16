import gspread
import pandas as pd
# from google.oauth2.service_account import Credentials
# from google.oauth2 import service_account
import pygsheets


# define the scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


client = pygsheets.authorize(
    service_account_file='/Users/amadu/besd-scraper-527f183dac48.json')


def getCurrentData():
    # get the instance of the Spreadsheet
    sheet = client.open("BeSD sources tracker")

    # get the first sheet of the Spreadsheet
    sheet_instance = sheet.get_worksheet(0)

    # get all the records of the data
    records_data = sheet_instance.get_all_records()

    # convert the json to dataframe
    old_data = pd.DataFrame.from_dict(records_data)
    old_data.to_csv("old_sources.csv")
    return 0


def updateSources(sheetname="Test_updateFromPython"):
    # get the instance of the Spreadsheet
    sheet = client.open("BeSD sources tracker")
    print(sheetname)
    # get the Import 10-Mar-2022 sheet
    # sheet_instance = sheet.get_worksheet(2)
    sheet_instance = sheet.worksheet_by_title(sheetname)
    print("You are going to update the google spreadsheet file " +
          sheetname + " with the data in new_sources.csv")
    data = pd.read_csv('new_sources.csv')
    sheet_instance.set_dataframe(data, start=(1, 1), copy_index=False, copy_head=True,
                                 extend=False, fit=False, escape_formulae=False)
    print("Google spreadsheet file successfully updated !")

    return 0
