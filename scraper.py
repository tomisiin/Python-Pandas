#import packages that enable web scraping
from bs4 import BeautifulSoup
import requests

#assign website to be scraped to a variable called 'url'
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

#check if requests is getting data from the website. 200 if everything is fine. Other error codes if not
requests.get(url)

#Assign to variable 'page' so it can be used later
page = requests.get(url)

#import contents of page variable and encode as html
soup = BeautifulSoup(page.text, 'html')

#view contents of soup variable
print(soup)

#use indexing to point to particular table in list of tables on the page
table = soup.find_all('table')[1]

#find all table headers and assign to 'world_titles' variable
world_titles = table.find_all('th')
world_titles

#use for loop to create a list of titles above and assign to new variable after performing text strip 
world_table_titles = [titlesss.text.strip() for titlesss in world_titles]
print(world_table_titles)

#import pandas package
import pandas as pd

#create new dataframe containing the titles above and display 
df = pd.DataFrame(columns = world_table_titles)
df

#back to scraped table, find all rows
col_data = table.find_all('tr')

#use for loop to append all the individual rows to the dataframe. [1:] is used 
for row in col_data[1:]:
    row_data = row.find_all('td')
    world_table_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = world_table_data

#view complete table in pandas dataframe
df

#to export the dataframe as a CSV file and save on local PC in a folder called Folder_for_Scraping
df.to_csv(r'C:\Users\...\...\Folder_for_Scraping\Companies.csv', index= False)
