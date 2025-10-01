from Sorter import Sort

DataHandler = Sort({
    "Name": ["Alice", "Bob"],
    "Age": [30, 25],
    "Country": ["USA", "Canada"]
}, False)

DataHandler.exportJson(DataHandler.resortData("Country"), "finale.json")
DataHandler.exportSheets(DataHandler.resortData("Country"), "final.xlsx", False)
DataHandler.exportSheets(DataHandler.resortData("Country"), "final.xlsx", True)
