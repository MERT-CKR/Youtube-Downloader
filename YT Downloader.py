from pytube import YouTube 
import os 

# Find the desktop automatically and format it as an escape character
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
desktop_path = desktop_path.replace("\\", r"\\")

# url input from user 
yt = YouTube( 
    str(input("Enter the URL of the video you want to download: \n>> "))) 
  
# extract only audio 
video = yt.streams.filter(only_audio=False).first() 
  
# download the file 
out_file = video.download(output_path = desktop_path) 
  
# save the file 
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 
  
# result of success 
print(yt.title + " has been successfully downloaded.")
