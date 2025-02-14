import streamlit as st
import requests
import os

# Set the backend URL (change if your backend runs elsewhere)
backend_url = "http://127.0.0.1:8000/process_audio/"

# Streamlit UI Components
st.title("Lip-Sync Avatar Video Generator")
st.write("Upload an audio file and an image to generate a lip-syncing avatar video.")

# File upload for audio and image
audio_file = st.file_uploader("Upload your audio file", type=["mp3", "wav", "ogg"])
image_file = st.file_uploader("Upload an image for the avatar", type=["jpg", "jpeg", "png"])

# Process the uploaded files when the button is clicked
if st.button("Generate Lip-Sync Avatar"):
    if audio_file is not None and image_file is not None:
        # Read the audio and image files
        audio_content = audio_file.read()
        image_content = image_file.read()

        # Prepare the files to be sent to the backend
        files = {
            'audio': ('audio.wav', audio_content, 'audio/wav'),
            'image': ('image.jpg', image_content, 'image/jpeg')
        }

        # Make the POST request to the backend
        try:
            with st.spinner("Processing..."):
                response = requests.post(backend_url, files=files)

                if response.status_code == 200:
                    result = response.json()

                    # Check if video was generated successfully
                    if "video_path" in result:
                        st.success("Avatar video generated successfully!")
                        st.video(result["video_path"])  # Display the video
                    else:
                        st.error(f"Error: {result.get('error', 'Unknown error')}")
                else:
                    st.error("Failed to communicate with the backend.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please upload both an audio file and an image.")
