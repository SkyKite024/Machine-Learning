import os
import requests
from moviepy import *
from pydub import AudioSegment
from pydub.playback import play

# Set your ElevenLabs API key
ELEVENLABS_API_KEY = "your_elevenlabs_api_key"

# Step 1: Extract audio from video
def extract_audio_from_video(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)
    print(f"Audio extracted to {output_audio_path}")

# Step 2: Transcribe audio to text (using OpenAI Whisper API or another service)
def transcribe_audio(audio_path):
    # Placeholder for transcription. Replace with actual API call to OpenAI Whisper or another service.
    transcription = "This is a sample transcription of the audio."
    print(f"Transcribed text: {transcription}")
    return transcription

# Step 3: Generate dubbed audio using ElevenLabs API
def generate_dubbed_audio(text, output_audio_path, voice="Rachel"):
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {
        "Authorization": f"Bearer {ELEVENLABS_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "text": text,
        "voice": voice
    }
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_audio_path, "wb") as f:
            f.write(response.content)
        print(f"Dubbed audio saved to {output_audio_path}")
    else:
        print(f"Error generating audio: {response.status_code}, {response.text}")

# Step 4: Replace audio in the video
def replace_audio_in_video(video_path, new_audio_path, output_video_path):
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(new_audio_path)
    video = video.set_audio(new_audio)
    video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    print(f"Dubbed video saved to {output_video_path}")

# Main script
if __name__ == "__main__":
    video_path = "input_video.mp4"  # Replace with your input video file
    audio_path = "extracted_audio.wav"
    dubbed_audio_path = "dubbed_audio.wav"
    output_video_path = "output_video.mp4"
    
    # Step 1: Extract audio
    extract_audio_from_video(video_path, audio_path)
    
    # Step 2: Transcribe audio
    transcription = transcribe_audio(audio_path)
    
    # Step 3: Generate dubbed audio
    generate_dubbed_audio(transcription, dubbed_audio_path)
    
    # Step 4: Replace audio in the video
    replace_audio_in_video(video_path, dubbed_audio_path, output_video_path)
