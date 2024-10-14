# import os
import csv
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin


# def get_all_links(url, domain):
#     """Scrapes the webpage for all the internal links."""
#     links = set()
    
#     try:
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         for a_tag in soup.find_all('a', href=True):
#             href = a_tag['href']
#             full_url = urljoin(url, href)
            
#             # Only keep internal links
#             if domain in full_url:
#                 links.add(full_url)
#     except requests.RequestException as e:
#         print(f"Error fetching {url}: {e}")
    
#     return links


# def crawl_website(base_url):
#     visited = set()
#     to_visit = set([base_url])
#     domain = base_url.split("//")[-1].split("/")[0]

#     while to_visit:
#         url = to_visit.pop()
#         if url not in visited:
#             visited.add(url)
#             print(f"Scraping {url}")
            
#             # Scrape and store the content
#             scrape_website(url)

#             # Get new links to visit
#             new_links = get_all_links(url, domain)
#             to_visit.update(new_links - visited)
#     print("done")




# def scrape_website(url):
#     # Fetch and parse the website content
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # Extract relevant data (modify as needed)
#     data = []
#     for element in soup.find_all(['div', 'article', 'section' ]):
#         data.append(element.text.strip())

#     # File path
#     file_path = 'morgan_edu_data.csv'
    
#     # Check if the file exists to decide whether to write headers or not
#     file_exists = os.path.isfile(file_path)
    
#     # Append data to CSV
#     with open(file_path, 'a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         # Write header only if the file does not exist
#         if not file_exists:
#             writer.writerow(['Content'])
#         # Write the data
#         for item in data:
#             writer.writerow([item])


# crawl_website("https://www.morgan.edu/computer-science/faculty-and-staff")


import scrapy
from urllib.parse import urljoin

class MorganEduSpider(scrapy.Spider):
    name = 'morgan_edu'
    start_urls = ['https://www.morgan.edu']
    allowed_domains = ['morgan.edu']

    # Add essential pages to scrape
    essential_pages = [
        '/academics',
        '/admissions',
        '/research',
        '/about',
        '/scmns/computerscience',
        '/computer-science/degrees-and-programs',
        '/computer-science/degrees-and-programs/ms_advancedcomputing',
        '/preview_program.php?catoid=24&poid=5398&returnto=1670',
        '/computer-science/degrees-and-programs/phd_advcomputing',
        '/computer-science/current-students/internship-opportunities',
        '/computer-science/current-students',
        '/computer-science/current-students/sacs',
        '/computer-science/admission-and-application',
        '/computer-science/faculty-and-staff/shuangbao-wang',
        '/computer-science/faculty-and-staff',
        '/computer-science/research'
    ]


    def __init__(self, *args, **kwargs):
        super(MorganEduSpider, self).__init__(*args, **kwargs)
        self.csv_file = open('morgan_edu_data2.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['url', 'content'])  # Write header

    def parse(self, response):
        # Extract content from current page
        content = ' '.join(response.css('p::text, h1::text, h2::text, h3::text').getall())
        
        # Write to CSV
        self.csv_writer.writerow([response.url, content])

        # Follow links to essential pages
        for page in self.essential_pages:
            full_url = urljoin(response.url, page)
            yield scrapy.Request(full_url, callback=self.parse)

    def closed(self, reason):
        self.csv_file.close()


