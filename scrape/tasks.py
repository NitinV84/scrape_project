from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from .models import Proxy
import time


@shared_task
def scrape_proxy_data():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration

    # Initialize a Chrome webdriver with headless mode
    with webdriver.Chrome(options=chrome_options) as driver:
        url = 'https://geonode.com/free-proxy-list'

        driver.get(url)

        # Wait for 1 sec for dynamic content to load 
        time.sleep(1)  
        html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table')

    # Process the table content
    if table:
        # Extract the rows from the table
        rows = table.find_all('tr')[1:]
        
        # Process the rows
        proxies_data = []
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 7:  
                ip = cols[0].text
                port = cols[1].text
                protocol = cols[3].text
                country = cols[4].text
                uptime = cols[6].text
                proxies_data.append({'ip': ip, 'port': port, 
                                     'protocol': protocol,
                                     'country': country, 'uptime': uptime})
            else:
                print("Invalid row format")
        
        # Print data
        for data in proxies_data:
            print(data)
        
        for data in proxies_data:
            Proxy.objects.create(**data)
    else:
        print("Table not found")
        

if __name__ == "__main__":
    scrape_proxy_data()
