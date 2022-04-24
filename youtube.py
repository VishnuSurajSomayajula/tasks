from pytube import YouTube


link = "https://www.youtube.com/watch?v=EAYlckSaviI"
s1 = YouTube(link)

print(s1.title)

video = s1.streams.all()
vid = list(enumerate(video))

for i in vid:
    print(i)
print()
stm = int(input("enter : "))
video[stm].download()
print("successfully")