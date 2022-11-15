

from pytube import YouTube
yt = YouTube('&quot;https://www.youtube.com/watch?v=n06H7OcPd-g&quot;')
yt = yt.get('mp4', '720p')
yt.download('/path/to/download/directory')


YouTube('video_url').streams.first().download('save_path')


YouTube('video_url').streams.first().download('C:\\Users\\username\\save_path')




from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])


