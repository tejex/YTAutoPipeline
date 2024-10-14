import os
import sys
from openai import OpenAI

class ScriptGenerator:
    def __init__(self, rawText) -> None:
        self.rawText = rawText
        self.script = None
        self.client = OpenAI(
            api_key = os.getenv("OPEN_AI_KEY")
        )
        
        self.generateScript()
    
    def generateScript(self):
        
        prompt = f""" You are tasked with generating a script for a YouTube video that tells the story of a historical figure in a hagiographical style. This style focuses on saints, martyrs, or revered figures, emphasizing their spiritual virtues, unwavering faith, and miraculous events. The narrative should reflect the strength, devotion, and divine intervention typically seen in such accounts. Use the raw text provided below to create a script that is both engaging and informative, intended solely for audio recording.

        Raw Text: {self.rawText}

        Instructions:

        Begin by introducing the person's name and ensure the story honors their virtues and faith.

        Avoid casual greetings such as "Hello" or "Welcome" and keep the tone reverent and storytelling in nature.

        Ensure the narrative focuses on faith, miracles, and endurance.

        The script should be as simple as possible, using basic words suitable for a 10th grader. Avoid using big words or overly complex vocabulary.

        The script should be engaging, clear, and suitable for a 3 to 5-minute audio recording.

        ANY time you have to write ANY names in the script, use SSML <phoneme> tags with accurate IPA phonemes to specify the correct pronunciation:

        Ensure the IPA phonemes accurately represent the intended pronunciation of the name.

        Double-check the IPA transcription for correctness.

        Ensure the SSML <phoneme> tags are correctly formatted, with proper opening and closing tags, and that all attributes are properly quoted.

        Example: If the name "Longinus" is pronounced "lon-GEE-nus" (with "GEE" as in "geese"), the correct IPA transcription would be lɒnˈdʒiːnəs. You should write:

        <phoneme alphabet="ipa" ph="lɒnˈdʒiːnəs">Longinus</phoneme>

        Apply this method consistently for all instances of the name and any other uncommon names in the script.

        Refrain from including visual elements, scene descriptions, or promotional language such as "like and subscribe."

        The story should evoke admiration for the figure's spiritual strength, in line with traditional hagiographical storytelling.

        Thank you.

        Additional Guidance:

        Accurate IPA Transcriptions:

        Use reliable resources or IPA dictionaries to find the correct IPA pronunciation matching the intended pronunciation of each name.

        For example, "Cappadocia" pronounced "kah-pah-DOH-see-ah" would have the IPA transcription kæpəˈdoʊʃiə, so you would write:

        <phoneme alphabet="ipa" ph="kæpəˈdoʊʃiə">Cappadocia</phoneme>

        Correct SSML Syntax:

        Ensure that every <phoneme> tag is properly opened and closed.

        Attribute values should be enclosed in double quotes.

        Example of correct syntax:

        <phoneme alphabet="ipa" ph="phonemes_here">NameHere</phoneme>

        Consistency:

        Treat all occurrences of each name consistently throughout the script.

        Double-check the script to ensure all SSML tags are correctly applied.

        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # You can specify "gpt-4" for the GPT-4 model
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2500  # Adjust token limit as per your needs
            )
            
            # Extract the generated script from the response
            self.script = response.choices[0].message.content

            return self.script
        
        except Exception as e:
            print(f"Error generating script: {e.message}")
            return None