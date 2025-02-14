from pydub import AudioSegment
import os

# Manually set FFmpeg paths
AudioSegment.converter = r"C:\ffmpeg-latest-win64-shared\ffmpeg-latest-win64-shared\bin\ffmpeg.exe"
AudioSegment.ffmpeg = r"C:\ffmpeg-latest-win64-shared\ffmpeg-latest-win64-shared\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg-latest-win64-shared\ffmpeg-latest-win64-shared\bin\ffprobe.exe"
