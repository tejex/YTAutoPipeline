
from Scrapers.infoScraper import InfoScraper
from Generators.scriptGen import ScriptGenerator


class YouTubeAV:
    def __init__(self,url) -> None:
        self.infoScraper = InfoScraper(url)
        self.rawInfo = None
        self.script = None
        self.audio = None
        
        self.rawInfo = self.infoScraper.getRawText()
        self.generateScript()
        
    def generateScript(self):
        if(not self.rawInfo):
            self.rawInfo = self.infoScraper.getRawText()
        
        
        self.script = ScriptGenerator(self.rawInfo)
        
        
        
        return self.script
        

def main():
    url = "https://www.oca.org/saints/lives/2024/09/17/102642-martyr-theodota-at-nicea"
    autoYT = YouTubeAV(url)

if __name__ == "__main__":
    main()