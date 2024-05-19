import pandas as pd

# First install pandas and openpyxl
# pip install pandas
# pip install openpyxl

'''
Goal: To read an Excel file using pandas and in later files change and manipulate the data because we hate the system and we shall overthrow it.
'''

# Read an Excel file
df = pd.read_csv('Classroom.csv')

# Display entire csv file
print(df)
