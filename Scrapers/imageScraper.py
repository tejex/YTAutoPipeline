import requests
import os
from PIL import Image
from io import BytesIO
import hashlib

class ImageScraper:
    def __init__(self, cse_id, api_key):
        self.cse_id = cse_id
        self.api_key = api_key

    def search_images(self, query,num_images=10):
        image_urls = []
        seen_urls = set()
        url = 'https://www.googleapis.com/customsearch/v1'
        max_results = 100  # Google API allows up to 100 results per query
        num_images = min(num_images, max_results)
        start_index = 1

        while len(image_urls) < num_images and start_index <= max_results:
            params = {
                'q': query,
                'cx': self.cse_id,
                'key': self.api_key,
                'searchType': 'image',
                'num': min(10, num_images - len(image_urls)),
                'start': start_index,
                'imgSize': 'large',
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                search_results = response.json()

                if 'items' in search_results:
                    for item in search_results['items']:
                        link = item['link']
                        if link not in seen_urls:
                            seen_urls.add(link)
                            image_urls.append(link)
                    start_index += 10
                else:
                    break  # No more results available
            except Exception as e:
                print(f"Error fetching images: {e}")
                break
        return image_urls

    def downloadImages(self, urlList, save_dir='downloaded_images'):
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        
        seen_hashes = set()
        downloaded = 0
        for idx, url in enumerate(urlList, start=1):
            try:
                # Send a GET request to the URL
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                # Open the image using PIL
                image = Image.open(BytesIO(response.content))

                # Compute the hash of the image
                image_hash = hashlib.md5(response.content).hexdigest()
                if image_hash in seen_hashes:
                    print(f"Duplicate image detected (hash): {url}")
                    continue
                else:
                    seen_hashes.add(image_hash)

                # Define the image filename
                image_name = f'image_{idx}.png'

                # Save the image as PNG
                image.save(os.path.join(save_dir, image_name), 'PNG')
                print(f"Downloaded and saved as: {image_name}")
                downloaded += 1
            except requests.RequestException as e:
                print(f"Failed to download {url}: {e}")
            except Exception as e:
                print(f"Failed to process {url}: {e}")
            if downloaded >= len(urlList):
                break