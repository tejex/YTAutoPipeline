
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