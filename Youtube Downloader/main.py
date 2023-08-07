from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There has been error downloading the video")
    print("The download has been successfully made")


link = input(f"Put your Youtube Link Here - URL:")
Download(link)