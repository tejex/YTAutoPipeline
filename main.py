from Scrapers.infoScraper import InfoScraper


class YT_Auto_Video:
    def __init__(self,url,infoScraper) -> None:
        self.infoScraper = InfoScraper(url)
        self.rawInfo = None
        self.script = None
        self.audio = None
    
    def generateScript(self):
        #make call to GPT API 




def main():
    url = "https://www.oca.org/saints/lives/2024/09/17/102642-martyr-theodota-at-nicea"

    scraper = InfoScraper(url)
    rawText = scraper.getRawText()


if __name__ == "__main__":
    main()