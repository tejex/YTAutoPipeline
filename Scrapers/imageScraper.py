import urllib.request
from bs4 import BeautifulSoup
import requests
import os
from PIL import Image
from io import BytesIO

class ImageScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def scrape_images(self):
        # Fetch the page
        request = urllib.request.Request(self.url, headers=self.headers)
        response = urllib.request.urlopen(request)
        page_info = BeautifulSoup(response, 'html.parser')

        # Find image elements
        images = page_info.find_all('img')
        image_urls = []

        for img in images:
            img_url = img.get('src')
            if img_url and img_url.startswith('http'):
                image_urls.append(img_url)

        return image_urls

    def downloadImages(self, urlList, save_dir='downloaded_images'):
        
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        for url in urlList:
            try:
                # Send a GET request to the URL
                response = requests.get(url)
                response.raise_for_status()  # Raise an error for bad responses

                # Open the image using PIL
                image = Image.open(BytesIO(response.content))

                # Extract the image name from the URL and change extension to .png
                image_name = os.path.splitext(os.path.basename(url))[0] + '.png'

                # Save the image as PNG
                image.save(os.path.join(save_dir, image_name), 'PNG')
                print(f"Downloaded and saved as: {image_name}")

            except requests.RequestException as e:
                print(f"Failed to download {url}: {e}")
            except Exception as e:
                print(f"Failed to process {url}: {e}")

