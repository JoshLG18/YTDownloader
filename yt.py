from pytubefix import YouTube

try:
    url = input("Enter the YouTube URL: ")
    yt = YouTube(url)
    print("Title:", yt.title)
    print("Views:", yt.views)

    streams = yt.streams.filter(res="1080p", file_extension='mp4')
    if streams:
        yd = streams.first()
        yd.download()
    else:
        print("1080p stream not available, downloading highest resolution instead.")
        yd = yt.streams.get_highest_resolution()
        yd.download()

    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))



