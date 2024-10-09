import os

import tkinter as tk

from Scrapers.infoScraper import InfoScraper
from Generators.scriptGen import ScriptGenerator
from Generators.audioGen import AudioGenerator
from Scrapers.imageScraper import ImageScraper

class YouTubeAV:
    def __init__(self,url, imagesURL) -> None:
        self.api_key = os.getenv('API_KEY')
        self.cse_id = os.getenv('CSE_ID')
        self.infoScraper = InfoScraper(url)
        self.imageScraper = ImageScraper(self.cse_id, self.api_key)
        
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
        print(self.script)
        self.generateAudio()
        
        return self.script

    def generateAudio(self):
        if(not self.script):
            self.generateScript()
        
        self.audioPath = AudioGenerator(self.script)
    
        return self.audioPath

    def collectImages(self, query):
        scraper = self.imageScraper
        num_images = 20  # Number of images to download
        image_urls = scraper.search_images(query,num_images=num_images)
        scraper.downloadImages(image_urls, save_dir='images')
        

def main():
    def on_submit():
        url = urlEntry.get() 
        if url:
            image_url = "https://www.google.com/search?q=saint+theodota+and+3+sons"
            autoYT = YouTubeAV(url, image_url)
            autoYT.collectImages("Apostle Mark of the Seventy Icons")
        else:
            print("Please enter a valid URL.")

    # Create the main window
    window = tk.Tk()
    window.geometry("1000x320+350+100")
    window.title("YouTube Automation")

    # Create UI elements
    urlLabel = tk.Label(window, text="Enter the URL:")
    urlLabel.pack(pady=10)
    
    # imageSearchLabel = tk.Label(window, text="Enter the name of the Icon:")
    # imageSearchLabel.pack(pady=10)
    
    # imageSearchEntry = tk.Entry(window, width=50)
    # imageSearchEntry.pack(pady=50)

    urlEntry = tk.Entry(window, width=50)
    urlEntry.pack(pady=10)

    submit_button = tk.Button(window, text="Submit", command=on_submit)
    submit_button.pack(pady=10)

    # Start the Tkinter event loop
    #https://www.oca.org/saints/lives/2024/04/25/101204-apostle-and-evangelist-mark
    window.mainloop()

if __name__ == "__main__":
    main()

