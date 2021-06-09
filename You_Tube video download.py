from pytube import YouTube

link = input("Enter the link : ")
yt = YouTube(link)

videos = yt.streams.all()

for video in videos:
    z = str(video)
    print(str(z+"\n"))

tag = int(input("Enter the tag number : "))
video = yt.streams.get_by_itag(itag = tag)
video.download()


#or video.download("Y:\\")
