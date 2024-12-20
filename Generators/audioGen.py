import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs


class AudioGenerator:
    def __init__(self, script) -> None:
        self.script = script
        self.client = ElevenLabs(api_key=os.getenv("ELEVEN_LABS_KEY"))
        self.audio = None
        self.audio_file_counter = 0
        self.generateAudio()
        
    
    def generateAudio(self):
                
        response = self.client.text_to_speech.convert(
            voice_id="pqHfZKP75CvOlQylNhV4", # Adams voice
            output_format="mp3_22050_32",
            text=self.script,
            model_id="eleven_turbo_v2", # use the turbo model for low latency
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
                    
        audioFilePath = f"audio{self.audio_file_counter}.mp3"

        with open(audioFilePath, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)

        self.audio_file_counter += 1
                    
        print(f"A new audio file was saved successfully!")
        return audioFilePath