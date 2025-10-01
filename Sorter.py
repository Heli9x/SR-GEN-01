import pandas as pd
import json

class Sort:
    def __init__(self, data, is_file=True):
        if is_file:
            if data.endswith(".xlsx"):
                self.dataFrame = pd.read_excel(data)
            elif data.endswith(".csv"):
                self.dataFrame = pd.read_csv(data)
            else:
                raise ValueError("Unsupported file format try .xlsx or .csv")
        else:
            self.dataFrame = pd.DataFrame(data)

    def deleteColumn(self, columnName):
        """
        Deletes a column from the DataFrame if it exists.
        """
        if columnName in self.dataFrame.columns:
            self.dataFrame = self.dataFrame.drop(columns=[columnName])
        else:
            print(f"Column '{columnName}' does not exist.")
        return self.dataFrame

            
    def clean(self, columnName, numberOfDuplicateColumns):
        dupes = [col for col in self.dataFrame.columns if col.startswith(f"{columnName}.")]
        if numberOfDuplicateColumns is not None:
            dupes = dupes[:numberOfDuplicateColumns]

        self.dataFrame = self.dataFrame.drop(columns=dupes, errors="ignore")
        return self.dataFrame

    def rarefy(self, columnName: str):
        elements = self.dataFrame[columnName].unique().tolist()
        return elements

    def addUniqueIdColumn(self, columnName="UniqueID", start=1):
        """
        Adds a new column with unique numbered IDs to the DataFrame.
        By default, the column is named 'UniqueID' and starts from 1.
        """
        self.dataFrame[columnName] = range(start, start + len(self.dataFrame))
        return self.dataFrame

    def resortData(self, columnName:str):
        """
            This function creates an array of dataframes sorted according to the unique list of data provided.
            The Data in the filtered column elements must be members of column name in the originall data.
            if there's no relation, an error will occur or the data will not be rendered properly.
        """
        resortedData = {key: df for key, df in self.dataFrame.groupby(columnName)}
        return resortedData
    
    def exportSheets(self, data:dict, filename="final.xlsx",  singular=True):
        """
            This function exports a single work book, containing sheets created from the resorted data function as data frames.
            if xlsxwriter is missing or encounters an error, try to install it through pip manually. Command: 'pip install Xlsxwriter'.
        """
        with pd.ExcelWriter(filename, engine="xlsxwriter") as exporter:
            if singular:
                self.dataFrame.to_excel(exporter, sheet_name=self.dataFrame.columns[0], index=False)
            else:
                for sheet, df in data.items():
                    safe_name = str(sheet)[:31]
                    df.to_excel(exporter, sheet_name=safe_name, index=False)
        print("done")

    def exportJson(self, data:dict, filename="final.json"):
        json_data = {str(sheet): df.to_dict(orient="records") for sheet, df in data.items()}
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print("done")
