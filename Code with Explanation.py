#Python library to download youtube videos
from pytube import YouTube

#Enter the link here
link = input("Enter the link : ")
yt = YouTube(link)

#It will display all the options
videos = yt.streams.all()

#To display the options line by line
for video in videos:
    z = str(video)
    print(str(z+"\n"))

#For to enter the itag value   
tag = int(input("Enter the tag number : "))

#According to your itag value it will download the video
video = yt.streams.get_by_itag(itag = tag)
video.download()
