import pytube


link = input("Link to the video: ")
yt = pytube.YouTube(link)

valid_format = False

while (not (valid_format)):
    format = input("mp4 or 3gpp? ")
    if (format == "mp4"):
        stream = yt.streams.filter(file_extension='mp4').first()
        valid_format = True
    elif (format == "3gpp"):
        stream = yt.streams.first()
        valid_format = True

stream.download()
