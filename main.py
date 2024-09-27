
from Scrapers.infoScraper import InfoScraper
from Generators.scriptGen import ScriptGenerator
from Generators.audioGen import AudioGenerator
from Scrapers.imageScraper import ImageScraper

class YouTubeAV:
    def __init__(self,url, imagesURL) -> None:
        self.infoScraper = InfoScraper(url)
        # self.imageScraper = ImageScraper(imagesURL)
        self.rawInfo = None
        self.script = None
        self.audioPath = None
        
        self.rawInfo = self.infoScraper.getRawText()
        self.generateScript()

        
    def generateScript(self):
        if(not self.rawInfo):
            self.rawInfo = self.infoScraper.getRawText()
        
        scriptGen = ScriptGenerator(self.rawInfo)
        self.script = scriptGen.script    
        self.generateAudio()
        
        return self.script

    def generateAudio(self):
        if(not self.script):
            self.generateScript()
        
        self.audioPath = AudioGenerator(self.script)
    
        return self.audioPath

    def collectImages(self):
        images = self.imageScraper.scrape_images()
        self.imageScraper.downloadImages(images)
        

def main():
    url = "https://www.oca.org/saints/lives/2024/09/17/102642-martyr-theodota-at-nicea"
    imageURL = "https://www.google.com/search?q=saint+theodota+and+3+sons&sca_esv=2a0623079f1ec93f&sca_upv=1&udm=2&biw=1470&bih=832&sxsrf=ADLYWIKKMnbh6eMaUBg1iyihlVhVkynzUg%3A1727054682127&ei=WsPwZry4B5SiptQPweKY4Ak&ved=0ahUKEwi8zdeG9NeIAxUUkYkEHUExBpwQ4dUDCBA&uact=5&oq=saint+theodota+and+3+sons&gs_lp=Egxnd3Mtd2l6LXNlcnAiGXNhaW50IHRoZW9kb3RhIGFuZCAzIHNvbnNI3RlQ8gFYwxhwAngAkAEAmAFzoAGFBqoBBDExLjG4AQPIAQD4AQGYAgGgAgTCAgcQABiABBgYmAMAiAYBkgcBMaAHnAQ&sclient=gws-wiz-serp"
    # autoYT = YouTubeAV(url,imageURL)
    
    cse_id = ""
    api_key = ""

    query = "Peter The Apostle"
    scraper = ImageScraper(query, cse_id, api_key)
    num_images = 20  # Number of images to download
    image_urls = scraper.search_images(num_images=num_images)
    scraper.downloadImages(image_urls, save_dir='images')
    
    
if __name__ == "__main__":
    main()
