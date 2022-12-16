import pandas as pd


path = "Seminar on Emerging topics.xlsx"
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel(path)
print(dataframe1)