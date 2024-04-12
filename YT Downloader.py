import pytube
import moviepy.editor as mp
import os


from pytube import YouTube
from moviepy.editor import AudioFileClip

def youtube_to_mp3(url, filename):
    # Masaüstü yolunu al
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video_filename = os.path.join(desktop_path, filename + ".mp4")  # .mp4 uzantısını ekleyin
    video.download(filename=video_filename)

    # Ses dosyasını MP3 formatına dönüştür
    audio = AudioFileClip(video_filename)
    audio_filename = os.path.join(desktop_path, filename + ".mp3")
    audio.write_audiofile(audio_filename)

    # Orijinal dosyayı sil (isteğe bağlı)
    os.remove(video_filename)

# Kullanım örneği:


def youtube_to_mp4(url, filename):
  # Masaüstü yolunu al
  desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

  yt = pytube.YouTube(url)
  video = yt.streams.first()
  video.download(filename=os.path.join(desktop_path, filename))

def main():
    selection = int(input("mp3 için: 0\nmp4 için: 1 \n>> "))
    if selection !=1 and selection !=0:
      main()
    elif selection==0:
        link = input("İndirmek istediğiniz MP3 dosyasının Youtube linkini girin: \n>> ")
        youtube_to_mp3(link, "music")
    elif selection==1:
        link = input("İndirmek istediğiniz MP4 dosyasının Youtube linkini girin: \n>> ")
        youtube_to_mp4(link, "video.mp4")
main()
