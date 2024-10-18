import os
from os import listdir
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"

from PIL import Image
import pytesseract
import imagehash
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from moviepy.audio.fx.all import audio_loop



class VideoGenerator:
    def __init__(self):
        self.images = '/Users/bamlakdeju/Desktop/YTAutoPipeline/images/'
        self.videoCount = 0
        self.audioFile = f'/Users/bamlakdeju/Desktop/YTAutoPipeline/audio{self.videoCount}'
    
    def pieceVideoTogether(self):
        images = []
        unique_hashes = set()      
        
        for image in listdir(self.images):
            if (image.endswith(".png")):
                
                img = Image.open(self.images + image)
                hash_val = imagehash.average_hash(img)
                text = pytesseract.image_to_string(img)
                
                if hash_val in unique_hashes:
                    continue
                    
                unique_hashes.add(hash_val)
                
                if(not text.strip()):
                    images.append(image)    

        clips = []
        
        for image in images:
            clip = ImageClip(self.images + image).set_duration(25)
            clips.append(clip)
        
        audio = AudioFileClip(self.audioFile + '.mp3')

        slideshow = concatenate_videoclips(clips, method="compose")
        
        if audio.duration > slideshow.duration:
            audio = audio.subclip(0, slideshow.duration)
        elif audio.duration < slideshow.duration:
            audio = audio.fx(audio_loop, duration=slideshow.duration)
            
        slideshow = slideshow.set_audio(audio)

        slideshow.write_videofile(f"slideshow{self.videoCount}.mp4", fps=24, codec="libx264", audio_codec="aac",temp_audiofile="temp-audio.m4a", remove_temp=True,)
        self.videoCount += 1

        return