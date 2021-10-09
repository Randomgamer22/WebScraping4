#Importing all module required
import csv 
import pandas as pd

#Converting the data from the csv file to a dataframe using the pandas module
df = pd.read_csv("all_stars.csv")

#Using a the dropna() functionf which drops all the NAN values in the dataframe form all the columns
df = df.dropna()

#Removing the last 2 rows of the dataframe because the dropna function is not able to detect the last 2 rows. (Bug)
df = df.iloc[:-2]

#Using the to_csv function to write the data frame to a csv file
df.to_csv("cleaned_data.csv")
    

