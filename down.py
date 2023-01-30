from pytube import YouTube

def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("There was an error")
    print("Download succesful")


def run():
    url = input('URL of the video: ')
    download(url)


if __name__ == '__main__':
    run()

# URL = "Enter video URL"
# video = YouTube(URL)
# video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)

# video_streams.download(filename = "my first YouTube download2",
#  output_path = "video_path")