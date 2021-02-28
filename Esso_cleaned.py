import pandas as pd
#import xlsxwriter
import os
from datetime import datetime
from datetime import date

os.chdir(r'/Users/HomeFolder/Desktop')
# Setting up the time that the info was acquired and getting the date to use as part of the file name
today_date = date.today()
"""(r' /Insert?Path/To/File.Extensiontype') Is making the desktop the standard location for the access to the information from the xlsx file from supplier."""

df = pd.read_excel(
    r"/Users/HomeFolder/Desktop/Pricebook_ESSO COLLINGWOOD   NONCIG - 022125534.xlsx")  # Path is saved from site to desktop

# Select Columns to ready for export to new spreadsheet(s)
cols = [8, 1, 2, 4, 3]
df_clean = df[df.columns[cols]]

# Create price per unit column (rounded to 2 decimal places)
df_clean['$/unit'] = round(df_clean['Case Cost'] /
                           df_clean['Unit Size'], 2)

file_code = 'Esso_cleaned_Coremark'
file_name = f'{today_date}_{file_code}.csv'
# worksheet = file_name.add_worksheet(Clean Data)
# Exporting df to new database- using date to identify creation date and keep the index column from displaying as the first column

df_clean.to_csv(file_name, index=False)
# Delete original file downloaded to keep computer clean. ***Does NOT go to trash- it is permanently gone!
#  os.remove("/Users/HomeFolder/Desktop/00524268.xlsx")
#print('Old data has been removed')
print('DO NOT OPEN WITH EXCEL')
print('File has been created and ready for use on Desktop')
