prompt = f"""
        You are tasked with generating a script for a YouTube video that tells the story of a historical figure in a **hagiographical style**. This style focuses on saints, martyrs, or revered figures, emphasizing their spiritual virtues, unwavering faith, and miraculous events. The narrative should reflect the strength, devotion, and divine intervention typically seen in such accounts. Use the raw text provided below to create a script that is both engaging and informative, intended solely for audio recording. 

        **Raw Text:**
        {self.rawText}

        **Instructions:**
        - Begin by introducing the person's name and ensure the story honors their virtues and faith.
        - Avoid casual greetings such as "Hello" or "Welcome" and keep the tone reverent and storytelling in nature.
        - Ensure the narrative focuses on faith, miracles, and endurance, avoiding overly complex vocabulary.
        - The script should be engaging, clear, and suitable for a 3 to 5-minute audio recording.
        - Refrain from including visual elements, scene descriptions, or promotional language such as "like and subscribe."
        - The story should evoke admiration for the figure's spiritual strength, in line with traditional hagiographical storytelling.

        Thank you.
        """
