# Data Handler Documentation

A Python class for handling and manipulating data using pandas DataFrame.

## Table of Contents
- [Installation](#installation)
- [Class: Sort](#class-sort)
- [Methods](#methods)
  - [Constructor](#constructor)
  - [deleteColumn](#deletecolumn)
  - [clean](#clean)
  - [rarefy](#rarefy)
  - [addUniqueIdColumn](#adduniqueidcolumn)
  - [resortData](#resortdata)
  - [exportSheets](#exportsheets)
  - [exportJson](#exportjson)

## Installation

Required dependencies:
```bash
pip install pandas xlsxwriter
```

## Class: Sort

### Constructor
```python
Sort(data, is_file=True)
```
Creates a new Sort instance with either file data or dictionary data.

#### Parameters:
- `data`: Path to file (.xlsx or .csv) or dictionary data
- `is_file`: Boolean indicating if input is a file path (default: True)

#### Example:
```python
# From file
handler = Sort("data.xlsx")

# From dictionary
data = {
    "Name": ["Alice", "Bob"],
    "Age": [30, 25]
}
handler = Sort(data, is_file=False)
```

### Methods

#### deleteColumn
```python
deleteColumn(columnName)
```
Removes a specified column from the DataFrame.

##### Example:
```python
handler = Sort({"Name": ["Alice"], "Age": [30]}, False)
handler.deleteColumn("Age")
# Result: DataFrame with only "Name" column
```

#### clean
```python
clean(columnName, numberOfDuplicateColumns)
```
Removes duplicate columns that start with the specified column name.

##### Example:
```python
# If DataFrame has columns: ["Name", "Name.1", "Name.2"]
handler.clean("Name", 2)
# Result: Only "Name" column remains
```

#### rarefy
```python
rarefy(columnName)
```
Returns a list of unique values in the specified column.

##### Example:
```python
data = {
    "Country": ["USA", "Canada", "USA", "Mexico"]
}
handler = Sort(data, False)
unique_countries = handler.rarefy("Country")
# Result: ["USA", "Canada", "Mexico"]
```

#### addUniqueIdColumn
```python
addUniqueIdColumn(columnName="UniqueID", start=1)
```
Adds a new column with sequential unique IDs.

##### Example:
```python
handler = Sort({"Name": ["Alice", "Bob"]}, False)
handler.addUniqueIdColumn("ID", 100)
# Result: DataFrame with new "ID" column starting at 100
```

#### resortData
```python
resortData(columnName)
```
Groups data by unique values in the specified column.

##### Example:
```python
data = {
    "Country": ["USA", "Canada", "USA"],
    "Name": ["John", "Alice", "Bob"]
}
handler = Sort(data, False)
grouped = handler.resortData("Country")
# Result: Dictionary with DataFrames grouped by country
```

#### exportSheets
```python
exportSheets(data, filename="final.xlsx", singular=True)
```
Exports data to Excel file with multiple sheets.

##### Example:
```python
grouped_data = handler.resortData("Country")
handler.exportSheets(grouped_data, "output.xlsx", singular=False)
# Creates Excel file with separate sheets for each country
```

#### exportJson
```python
exportJson(data, filename="final.json")
```
Exports data to JSON file.

##### Example:
```python
grouped_data = handler.resortData("Country")
handler.exportJson(grouped_data, "output.json")
# Creates JSON file with data grouped by country
```

## Usage Example

```python
# Create handler from dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Country": ["USA", "Canada", "USA"],
    "Age": [25, 30, 35]
}
handler = Sort(data, is_file=False)

# Add unique IDs
handler.addUniqueIdColumn()

# Group by country
grouped = handler.resortData("Country")

# Export to Excel and JSON
handler.exportSheets(grouped, "output.xlsx", singular=False)
handler.exportJson(grouped, "output.json")
```
