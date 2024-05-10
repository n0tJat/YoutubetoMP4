from pytube import YouTube
from pytube import Stream

user_input = input(f"Paste Youtube url: ")

yt = YouTube(f'{user_input}')

stream = yt.streams.get_by_itag(22)
stream.download()

