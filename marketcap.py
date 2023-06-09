#Description: Scrape the top 10 cryptocurrencies by market cap.

#import the libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Create empty list to store data

crypto_name_list = []
crypto_marketcap_list = []
crypto_price_list = []
crypto_circulating_supply_list = []
crypto_symbol_list = []

#Create an empty dataframe to help organise the data

df = pd.DataFrame()

#Create a function to scrape the data
# Example: https://coinmarketcap.com/historical/20220821/
def scrape(date = '20220821/'):
    #Get the URL of the website that we want to scrape

    URL = 'https://coinmarketcap.com/historical/' +date
    #Make a request to the website 
    webpage = requests.get(URL)
    #Parse the text from the website
    soup = BeautifulSoup(webpage.text, 'html.parser')

    #Get the table row element
    tr = soup.find_all('tr', attrs={'class':'cmc-table-row'})
    #Create a count variable for the number of ccs that we want to scrape

    count = 0

    #Loop through every row to gather the data/ information
    for row in tr:
        #if the count is reached then break out of loop

      if count == 10:
        break;

    count = count + 1 #Increment count by 1

    #Store the name of the cc into a variable
    #Find the td element (or column) to later get cc name

    name_column = row.find('td', attrs={'class':'class="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name"'})
    crypto_name = name_column.find('a', attrs={'class':'cmc-table__column-name--name cmc-link'}).text.strip()
    #Store coin market cap of cc into a variable
    crypto_market_cap = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()
    #Find and store the crpyto price
    crypto_price = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()
    #Find and store the crypto supply and symbol
    crypto_circulating_supply_and_symbol = row.find('td', attrs = {'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
    #Split the data
    crypto_circulating_supply = crypto_circulating_supply_and_symbol.split(' ')[0]
    crypto_symbol = crypto_circulating_supply_and_symbol.split(' ')[1]

    #APPEND DATA TO THE LISTS

    crypto_name_list.append(crypto_name)
    crypto_marketcap_list.append(crypto_market_cap)
    crypto_price_list.append(crypto_price)
    crypto_circulating_supply_list.append(crypto_circulating_supply)
    crypto_symbol_list.append(crypto_symbol)

    #run the scrape function
    scrape(date = '20220821/')

    #Store thr data into a dataframe to help organize the data
    df['Name'] = crypto_name_list
    df['Market Cap'] = crypto_marketcap_list
    df['Price'] = crypto_price_list
    df['Circulating Supply'] = crypto_circulating_supply_list
    df['Symbol'] = crypto_symbol_list

    #Display the Data
    df



