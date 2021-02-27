import pandas as pd
import xlsxwriter
import os
from datetime import datetime
from datetime import date

os.chdir(r'/Users/HomeFolder/Desktop')
# Setting up the time that the info was acquired and getting the date to use as part of the file name
today_date = date.today()
now = datetime.now()
"""(r' /Insert?Path/To/File.Extensiontype') Is making the desktop the starting location for the access to the information from the xlsx file from supplier."""

df = pd.read_excel(
    r"/Users/HomeFolder/Desktop/Pricebook_ESSO COLLINGWOOD   NONCIG - 022125534.xlsx")  # Path is saved from site to desktop

# Select Columns to to keep for export to new file. (.csv)
cols = [1, 2, 3, 4, 8]
df_clean = df[df.columns[cols]]
# print(df_clean) #Testing output of dcleaned
# File output name creation
file_code = 'Esso_CoreMark_Prices'
file_name = f'{today_date}_{file_code}.csv'
# worksheet = file_name.add_worksheet(Import)
# Exporting df to new database- using date to identify creation date and keep the index column from displaying as the first column

writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df_clean.to_csv(writer, "Import", index=False)
writer.save()
# writer.close()

#print('New pricebook is ready')
#print('Old data has been removed')
print('File has been updated and ready for use on Desktop')
print('Thank you.')

# Delete original file downloaded to keep computer clean. ***Does NOT go to trash- it is permanently gone!
#os.remove("/Users/HomeFolder/Desktop/Pricebook_ESSO-COLLINGWOOD   NONCIG.xlsx")
