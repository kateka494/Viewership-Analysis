# Import Libraries

import pandas as pd
import numpy as pd 
import matplotlib.pyplot as plt

# Download dependencies

pip install openpyxl

data_path = "/Workspace/Users/katmathye0@gmail.com/Viewership Analysis .xlsx"

#Declaring a variable, df which will display the data in data_path when called
df= pd.read_excel(data_path)

#Displays the data with the excel file
display(df)

#The number of rows and columns
df.shape

#The column names
df.columns

#Displays the data types
df.dtypes

#Unique values from the 'VideoTitle' column
df['VideoTitle'].unique()

#Unique values from the 'platform' column
df['Platform'].unique()

df['TotalTimeWatched'].min()

df["TotalTimeWatched"].max()

#The sum of duplicates
df.duplicated().sum()

#Removing all the duplicates
df.drop_duplicates(inplace=True)


#New data without the duplicates
df.shape

#Display the number of unique vales
df['CustomerID'].nunique()

#This displays the actual list of unique values
display(df['CustomerID'].unique())
display(df['Platform'].unique())
display(df['PlayEventType'].unique())
display(df['VideoTitle'].unique())
display(df['DateID'].unique())
display(df['TotalTimeWatched'].unique())

#This displays the number of unique values
df['CustomerID'].unique()
df['Platform'].unique()
df['PlayEventType'].unique()
df['VideoTitle'].unique()
df['DateID'].unique()
df['TotalTimeWatched'].unique()


#The number of times platform occurs and creates a plot bar
pd.value_counts(df['Platform']).plot.bar(colormap="viridis_r")


# List all available colormaps in matplotlib 
display(plt.colormaps())

df.groupby("Platform")["TotalTimeWatched"].mean().plot(kind="bar", colormap="viridis_r") #This groups by the platform, timewatched mean and plot kind is the type of graph you want to display
plt.title("Average Total Time Watched per Platform")  
plt.xlabel("Platform")                                
plt.ylabel("Average Time Watched")                   
plt.show()  

#Displays how many times the playEvent occurs and creates a plot bar
df["PlayEventType"].value_counts().plot(kind="bar", colormap="viridis_r")
plt.title("Play Event Type Distribution")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.show()

Platform_share = df.groupby(
    "Platform"
)["TotalTimeWatched"].sum()

Platform_share.plot.pie(
    autopct='%1.1f%%',
    figsize=(8, 8)
)
plt.title("Platform Market Share")
plt.show()







