import requests
from bs4 import BeautifulSoup

class InfoScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.info = self.getInfo()
        
    def getInfo(self):
        
        try:
            response = requests.get(self.url)
            response.raise_for_status() 
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def getRawText(self):
        if self.info:
            # Remove script and style elements
            for script_or_style in self.info(['script', 'style']):
                script_or_style.decompose()
            
            # Get text and strip extra whitespaces
            raw_text = self.info.get_text(separator=' ')
            clean_text = ' '.join(raw_text.split())
            return clean_text
        return "Error fetching page"