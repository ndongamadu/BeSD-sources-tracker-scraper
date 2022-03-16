from scraper import *
from gsUpdate import *


def main():
    # get old data
    # getCurrentData()

    # get new data
    getData()
    print("====== Please verify the data and type YES if you want to update the google spreadsheet file\n")
    updateGS = input(
        "===== Update google spreadsheet ? !!! this action can't be undone \n")
    if (updateGS == "YES"):
        name = input(
            "=====Name of the sheet to be updated ? (default is Test_updateFromPython) \n")
        if name == "":
            name = "Test_updateFromPython"
        updateSources(name)
    return 0


if __name__ == '__main__':
    main()
