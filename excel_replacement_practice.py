import pandas as pd

# Make a new Data Frame (right click file name and hold down option key on mac)
df = pd.read_excel(
    '/Users/HomeFolder/Desktop/Pricebook_ESSO-COLLINGWOOD   NONCIG.xlsx')
print(df.head())
