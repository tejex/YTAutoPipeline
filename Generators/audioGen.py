import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs


class AudioGenerator:
    def __init__(self, script) -> None:
        self.script = script
        self.client = ElevenLabs(api_key="sk_e56e48e9a2aad8e768ec23a8d2961dfc12c4bbb028f2554b")
        self.audio = None
        self.generateAudio()
        
    
    def generateAudio(self):
                
        response = self.client.text_to_speech.convert(
            voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
            output_format="mp3_22050_32",
            text=self.script,
            model_id="eleven_turbo_v2_5", # use the turbo model for low latency
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
                    
        audioFilePath = f"{uuid.uuid4()}.mp3"

        with open(audioFilePath, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
                    
        print(f"A new audio file was saved successfully!")
        return audioFilePath