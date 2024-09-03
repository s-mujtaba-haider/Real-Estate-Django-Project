import requests
from bs4 import BeautifulSoup
import time
# URL of the search page

addresses = [
    "2430 E HOUSTON ST",
    "705 S SAN AUGUSTINE AVE",
    "2430 E HOUSTON ST",
    "705 S SAN AUGUSTINE AVE",
    "2430 E HOUSTON ST",
    "705 S SAN AUGUSTINE AVE",
    "0 SUMMA AVIATION",
    "2430 E HOUSTON ST",
    "2419 E HOUSTON ST",
    "705 S SAN AUGUSTINE AVE",
    "1319 WHITMAN AVE",
    "222 HOLY CROSS DR",
    "2430 E HOUSTON ST",
    "2419 E HOUSTON ST",
    "548 BABCOCK RD",
    "705 S SAN AUGUSTINE AVE",
    "1319 WHITMAN AVE",
    "222 HOLY CROSS DR",
    "0 EASTERLING",
    "936 FULTON AVE",
    "836 MENCHACA ST",
    "1700 VERA CRUZ",
    "216 ALAMOSA AVE",
    "25500 US HIGHWAY 281 S",
    "5471 BRONCO BILLY",
    "1138 GLADSTONE"
]

for addr in addresses:
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
    search_text = addr
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
    
    # Find all <a> tags within the search results
    all_links = search_results_soup.find_all('a')

    # Iterate through all links and find the one with "View Details" text
    for link in all_links:
        if "View Details" in link.get_text():
            href_value = link['href']
            break
    else:
        print("Link not found. for ->",url,addr)

    sec_url='https://bexar.trueautomation.com/ClientDB/'+href_value

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en-US,en;q=0.9",
        "Cookie": "__utma=137600931.1862651060.1717789972.1717796042.1718188319.3; __utmz=137600931.1718188319.3.2.utmcsr=upwork.com^|utmccn=(referral)^|utmcmd=referral^|utmcct=/; ApplicationGatewayAffinityCORS=a042ee949b4446b9285817cb6d393737; ApplicationGatewayAffinity=a042ee949b4446b9285817cb6d393737; ASP.NET_SessionId=f5ll5va30rh3q245rtityirq; __utmc=137600931; __utmb=137600931.6.10.1718188319",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }

    details_response = session.get(sec_url,headers=headers)
    details_soup = BeautifulSoup(details_response.content, 'html.parser')
    details_div = details_soup.find('div', class_='details')
    if details_div:
        # Extract the address information
        address_td = details_div.find('td', string='Address:')
        if address_td:
            address = address_td.find_next_sibling('td').get_text(separator='\n').strip()
            address=address.split(',')
            zip_code=address[-1].split(' ')[2]
            with open('zip_code.txt','a') as file:
                file.write(addr+"    "+str(zip_code))
                file.write('\n')

        else:
            print("Address not found.")
    else:
        print("Details div not found.")
    
    time.sleep(15)

