from gtts import gTTS
import moviepy.editor
import os

# Step 1: Convert Text to Speech (TTS)
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    audio_file = "audio.mp3"
    tts.save(audio_file)
    return audio_file

# Step 2: Create a Video with Image Background
def create_video_with_audio(image_file, audio_file, output_video_file):
    # Load the image and set the duration to match the audio length
    image_clip = ImageClip(image_file)
    
    # Load the audio file
    audio_clip = AudioFileClip(audio_file)
    
    # Set the duration of the image clip to the duration of the audio
    image_clip = image_clip.set_duration(audio_clip.duration)
    
    # Set the audio for the image clip
    video_clip = image_clip.set_audio(audio_clip)
    
    # Write the final video file
    video_clip.write_videofile(output_video_file, codec="libx264", fps=24)

# Step 3: Main function to put it all together
def text_to_video(text, image_file, output_video_file="output_video.mp4"):
    # Convert text to speech (save as audio file)
    audio_file = text_to_speech(text)
    
    # Create the video with the audio and image
    create_video_with_audio(image_file, audio_file, output_video_file)
    
    # Clean up the audio file after video creation
    os.remove(audio_file)
    print(f"Video saved as {output_video_file}")

# Example usage:
if __name__ == "__main__":
    # Sample text to convert to video
    text = "Welcome to this amazing video! Today, we are learning how to convert text to video."
    
    # Specify the image background for the video
    image_file = "background_image.jpg"  # Ensure you have an image file here
    
    # Call the function to create the video
    text_to_video(text, image_file)
