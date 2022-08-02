import wget
from moviepy.editor import VideoFileClip

import os

def gif_creater():
    video_url = str(input("Enter here TikTok video url: "))

    video_downloader = wget.download(video_url)
    video_creater = VideoFileClip(video_downloader)
    video_creater = video_creater.subclip(0, 4)
    video_creater.write_gif("TikTok_gif.gif")

    return os.path.abspath(r"TikTok_gif.gif")

if __name__ == "__main__":
    print(gif_creater())
