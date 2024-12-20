import os
import tkinter as tk

from Scrapers.infoScraper import InfoScraper
from Generators.scriptGen import ScriptGenerator
from Generators.audioGen import AudioGenerator
from Generators.videoGen import VideoGenerator
from Scrapers.imageScraper import ImageScraper
from Uploader.YT_Uploader import YouTubeUploader


class YouTubeAV:
    def __init__(self,url) -> None:
        self.api_key = os.getenv('API_KEY')
        self.cse_id = os.getenv('CSE_ID')
        self.infoScraper = InfoScraper(url)
        self.imageScraper = ImageScraper(self.cse_id, self.api_key)
        self.videoGenerator = VideoGenerator()
        self.youtubeUploader = YouTubeUploader("clientSecret.json","youtube", "v3", "https://www.googleapis.com/auth/youtube.upload")
        
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

    def collectImages(self, query):
        #scraping necessary images
        scraper = self.imageScraper
        num_images = 5 
        image_urls = scraper.search_images(query,num_images=num_images)
        scraper.downloadImages(image_urls, save_dir='images') 
    
    def generateVideo(self):
        self.videoGenerator.pieceVideoTogether()
    
    def uploadVideo(self,video_file_path):
        self.youtubeUploader.upload_video(video_file_path)
        pass

def main():
    def on_submit():
        url = urlEntry.get()
        imageQuery =  imageSearchEntry.get()
        if url:
            autoYT = YouTubeAV(url)
            # autoYT.collectImages(imageQuery)
            # autoYT.generateVideo()
            # autoYT.uploadVideo()
            autoYT.uploadVideo("/Users/bamlakdeju/Desktop/YTAutoPipeline/slideshow0.mp4")
        else:
            print("Please enter a valid URL.")
    
    window = tk.Tk()
    
    window.geometry("1000x320+350+100")
    window.title("YouTube Automation")

    # Configure the grid columns for proper alignment
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    # URL Label and Entry
    urlLabel = tk.Label(window, text="Enter the URL:")
    urlLabel.grid(row=0, column=0, padx=10, pady=10, sticky='E')

    urlEntry = tk.Entry(window, width=50)
    urlEntry.grid(row=0, column=1, padx=10, pady=10, sticky='W')

    # Image Search Label and Entry
    imageSearchLabel = tk.Label(window, text="Enter the name of the Icon:")
    imageSearchLabel.grid(row=1, column=0, padx=10, pady=10, sticky='E')

    imageSearchEntry = tk.Entry(window, width=50)
    imageSearchEntry.grid(row=1, column=1, padx=10, pady=10, sticky='W')

    # Submit Button
    submit_button = tk.Button(window, text="Submit", command=on_submit)
    submit_button.grid(row=2, column=0, columnspan=2, pady=20)

    window.mainloop()

if __name__ == "__main__":
    main()

