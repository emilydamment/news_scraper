from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://books.toscrape.com/"

page = requests.get(url) # Perform a GET request to the URL to retrieve the page content

soup = BeautifulSoup(page.text, 'html.parser') # Create a BeautifulSoup object to parse the HTML content of the page

titles = soup.find_all('h3') # Find all elements with the class 'title' in the parsed HTML

book_titles = []

for title in titles:
    link_tag = title.find('a') # Find the hyperlink tag within each book title element
    if link_tag and 'title' in link_tag.attrs: # Check if the link tag exists and has a 'title' attribute
        full_title = link_tag['title'] # If it does, asign to full_title
        book_titles.append(full_title) # And append to the list

data = {'book_titles': book_titles} # Create dictionary of titles

df = pd.DataFrame(data) # Convert to a Pandas dataframe

print(df.head()) # Display the dataframe