import os
import sys
from openai import OpenAI

class ScriptGenerator:
    def __init__(self, rawText) -> None:
        self.rawText = rawText
        self.script = None
        self.client = OpenAI(
            api_key = "sk-zpBQkeeEyFMTbiJI9Z1K0lGjrYmzTWH6XicVu4CtaVT3BlbkFJtc8oLRmjyTk9xpEee3udSF18X2098ljR6JnJ3aPoIA"
        )
        
        self.generateScript()
    
    def generateScript(self):
        
        prompt = f"""
        You are tasked with generating a script for a YouTube video that tells the story of Martyr Theodota at Nicea. Use the raw text provided below to create a script that focuses solely on the narrative part, intended for audio recording. The script should be engaging, informative, and have a storytelling tone suitable for a 3 to 5-minute video. Please ensure the content is specific to the provided raw text and does not include any scene descriptions or visual elements.
        
        **Raw Text:**
        {self.rawText}
        
        **Instructions:**
        - Always begin the script / story by stating the persons name and avoid saying anything like, Hello and welcome to our history teaching channel.
        - Don't use words that are too difficult to understand
        - Focus on the narrator's voice and storytelling aspects.
        - Make the narrative engaging and clear, suitable for an audio format.
        - Keep the script between 3 to 5 minutes long when read aloud.
        - Avoid any scene descriptions or visual elements.
        - Ensure the content reflects the details and tone from the raw text provided.
        - Avoid saying thank you for joining us today and dont ask for subscribers or for likes on the video.        
        Thank you.
        """
        
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # You can specify "gpt-4" for the GPT-4 model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2500  # Adjust token limit as per your needs
            )
            
            # Extract the generated script from the response
            self.script = response.choices[0].message.content.strip()
            print(self.script)
            return self.script
        
        except Exception as e:
            print(f"Error generating script: {e}")
            return None