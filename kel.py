from gtts import gTTS
import os

# Input text that you want to convert to speech
text_to_speak = "akash is lazy"

# Language in which you want to convert
language = 'en'  # 'en' for English, you can change to any supported language code

# Create gTTS object
tts = gTTS(text=text_to_speak, lang=language, slow=False)

# Save the speech to a file (MP3 format)
tts.save("output.mp3")

# Play the converted file (optional, can be skipped if not needed)
os.system("start output.mp3")  # For Windows, use 'start'. On macOS/Linux use 'open' or 'xdg-open'.
