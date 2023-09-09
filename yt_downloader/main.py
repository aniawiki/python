import pytube
from pydub import AudioSegment
import os

link = input("Link to the video: ")
yt = pytube.YouTube(link)

valid_format = False

while not valid_format:
    format = input("Choose the format (mp4 or mp3): ")
    stream = yt.streams.filter(file_extension='mp4').first()
    if (format == "mp4" or format == "mp3"):
        valid_format = True

video_path = stream.download()

file_name = input("Enter the desired file name (without extension): ")

audio = AudioSegment.from_file(video_path, format="mp4")
audio.export(f"{file_name}.{format}", format=format)

os.remove(video_path)
print(f"File {file_name}.{format} has been saved.")
