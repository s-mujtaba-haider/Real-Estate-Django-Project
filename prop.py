import requests
from bs4 import BeautifulSoup

# URL of the search page
url = "https://bexar.trueautomation.com/ClientDB/PropertySearch.aspx?cid=110"

# Common headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
}

# Step 1: Get the initial page to obtain the form data
session = requests.Session()
response = session.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the necessary form fields
viewstate = soup.find('input', {'id': '__VIEWSTATE'}).get('value')
viewstategen = soup.find('input', {'id': '__VIEWSTATEGENERATOR'}).get('value')
eventvalidation = soup.find('input', {'id': '__EVENTVALIDATION'}).get('value')

# Step 2: Submit the search request
search_text = "2430 E HOUSTON ST"
data = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategen,
    "__EVENTVALIDATION": eventvalidation,
    "propertySearchOptions:searchText": search_text,
    "propertySearchOptions:search": "Search",
    "propertySearchOptions:ownerName": "",
    "propertySearchOptions:streetNumber": "",
    "propertySearchOptions:streetName": "",
    "propertySearchOptions:propertyid": "",
    "propertySearchOptions:geoid": "",
    "propertySearchOptions:dba": "",
    "propertySearchOptions:abstract": "",
    "propertySearchOptions:subdivision": "",
    "propertySearchOptions:mobileHome": "",
    "propertySearchOptions:condo": "",
    "propertySearchOptions:agentCode": "",
    "propertySearchOptions:protestStatus": "",
    "propertySearchOptions:informalDate": "",
    "propertySearchOptions:formalDate": "",
    "propertySearchOptions:taxyear": "2024",
    "propertySearchOptions:propertyType": "All",
    "propertySearchOptions:orderResultsBy": "Owner Name",
    "propertySearchOptions:recordsPerPage": "25"
}

# Perform the POST request with the search parameters
search_response = session.post(url, headers=headers, data=data)

# Step 3: Parse the search results
search_results_soup = BeautifulSoup(search_response.content, 'html.parser')

# Print out the search results for demonstration
print(search_results_soup.prettify())
