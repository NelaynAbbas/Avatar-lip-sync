from fastapi import FastAPI, File, UploadFile
from pydub import AudioSegment
import cv2
import os
import numpy as np
from io import BytesIO

# Initialize FastAPI app
app = FastAPI()

# Ensure ffmpeg is installed
os.environ["FFMPEG_BINARY"] = "ffmpeg"

@app.post("/process_audio/")
async def process_audio(audio: UploadFile = File(...), image: UploadFile = File(...)):
    try:
        # Save the uploaded files temporarily
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as f:
            f.write(await audio.read())

        image_path = "temp_image.jpg"
        with open(image_path, "wb") as f:
            f.write(await image.read())

        # Process the audio file (you can modify this as needed)
        audio = AudioSegment.from_file(audio_path)
        modified_audio_path = "modified_audio.wav"
        
        # Example: Increase speed by 20% (you can apply other effects here)
        modified_audio = audio.speedup(playback_speed=1.2)
        modified_audio.export(modified_audio_path, format="wav")

        # Create a simple video from the uploaded image (for testing purposes)
        # OpenCV video creation
        video_output_path = "generated_avatar.mp4"
        frame_rate = 30
        frame_duration = int(1000 / frame_rate)  # Convert to milliseconds
        video_duration = len(modified_audio) / 1000  # Convert to seconds

        # Read image
        img = cv2.imread(image_path)
        height, width, layers = img.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify codec
        out = cv2.VideoWriter(video_output_path, fourcc, frame_rate, (width, height))

        # Generate frames (replicate the same image for the video)
        for _ in range(int(video_duration * frame_rate)):  # Number of frames
            out.write(img)  # Write the image as each frame

        out.release()

        # Clean up temporary files
        os.remove(audio_path)
        os.remove(image_path)
        os.remove(modified_audio_path)

        # Return the video path or video URL (In this case, we are assuming a locally saved video)
        return {"message": "Avatar video generated successfully!", "video_path": video_output_path}

    except Exception as e:
        return {"error": str(e)}
