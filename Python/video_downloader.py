from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import datetime
from colorama import *

def createFolder(folder_storage):
    print("=== Creating a new folder ===")
    os.mkdir('/home/' + os.environ.get('USER')+ '/' + folder_storage + '/')

def download(option, link, folder_storage):
    print(Fore.YELLOW)
    if option == 1 or option == 2:
        youtube = YouTube(link)
        stream = youtube.streams.filter(only_audio=True).first()
        stream.download(output_path='/home/' + os.environ.get('USER')+ '/' + folder_storage, filename=f"{youtube.title.replace(' ', '').lower()}.mp3")
        print(youtube.title.replace(' ', '').lower() + '.mp3\nDownloaded at ' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    else:
        print("The test for third option")
        playlist = Playlist(link)
        for video in playlist.video_urls:
            youtube = YouTube(video)
            stream = youtube.streams.filter(only_audio=True).first()
            stream.download(filename=f"{youtube.title.replace(' ', '').lower()}.mp3")
            print(youtube.title.replace(' ', '').lower() + '.mp3\nDownloaded at ' + datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))

    print("Folder storage: " + '/home/' + os.environ.get('USER')+ '/' + folder_storage)

print("+++++ Video Downloader +++++")

option = True

while option != 0:
    print(Fore.BLUE)
    print("++ Options ++\n0)Exit\n1)Download one vídeo\n2)Download more than one video\n3)Download a playlist")
    option = int(input("Choose an option: "))
    
    if option == 0:
        break
    else: 
        folder_storage = input("Type de Directory where you wanna storage the Download: ")
        try:
            #folder_storage = input("Type de Directory where you wanna storage the Download: ")
            if os.path.isdir(folder_storage) == False:
                createFolder(folder_storage)
            else:
                raise FileExistsError("The Folder exists")
        except FileExistsError:
           pass 
        
        if option == 1:
            link_of_video = input("Please type the link of the video what you wanna download: ")
            download(option, link_of_video, folder_storage)
        elif option == 2:
            number_of_videos = int(input("Please type how many videos you wanna download: "))
            for i in range(number_of_videos):
                link_of_video = input("Please type the link of the video what you wanna download: ")
                download(option, link_of_video, folder_storage)
        elif option == 3:
            link_of_playlist = input("Please type the link of the playlist what you wanna download: ")
            download(option, link_of_playlist, folder_storage)
        else:
            print("The option that you chosed is not available, please try another option")
print("Thanks for use this project!")

