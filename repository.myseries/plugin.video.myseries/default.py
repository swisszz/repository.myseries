# -*- coding: utf-8 -*-
import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import urllib.parse

addon_handle = int(sys.argv[1])
addon = xbmcaddon.Addon()

def build_url(query):
    return sys.argv[0] + '?' + urllib.parse.urlencode(query)

def list_series():
    # รายการตัวอย่าง (เปลี่ยนเป็นลิงก์จริงตามต้องการ)
    urls = [
        {"title": "ซีรีส์ตัวอย่าง 1", "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"},
        {"title": "ซีรีส์ตัวอย่าง 2", "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"}
    ]
    for item in urls:
        list_item = xbmcgui.ListItem(label=item["title"])
        list_item.setInfo("video", {"title": item["title"]})
        # สร้าง URL ที่พารามิเตอร์ mode=play และ url=ลิงก์วิดีโอ
        url = build_url({"mode": "play", "url": item["url"]})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

def play_video(video_url):
    play_item = xbmcgui.ListItem(path=video_url)
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)

if __name__ == '__main__':
    # ดึงพารามิเตอร์จาก sys.argv
    args = urllib.parse.parse_qs(sys.argv[2][1:])
    mode = args.get('mode', [None])[0]
    if mode == "play":
        url = args.get('url', [None])[0]
        if url:
            play_video(url)
    else:
        list_series()
