import urllib.request
from bs4 import BeautifulSoup

#  Created Scraper class
class Scraper:
    def __init__(self, site):
        self.site = site

    # def scrape(self):
    #     response = urllib.request.urlopen(self.site)
    #     html = response.read()
    #     parser = "html.parser"
    #     soup = BeautifulSoup(html, parser)
    #
    #     for tag in soup.find_all("a"):
    #         url = tag.get("href")
    #         if url is None:
    #             continue
    #         if "html" in url:
    #             print("\n" + url)

    # Scrape method that gets headlines and saves in a txt file.
    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        with open("output.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url and 'html' in url:
                    print("\n" + url)
                    f.write(url + "\n")

news = "https://news.google.com/"
Scraper(news).scrape()
