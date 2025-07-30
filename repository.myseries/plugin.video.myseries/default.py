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
    # ตัวอย่างแสดงรายการ 2 รายการ
    urls = [
        {"title": "ซีรีส์ตัวอย่าง 1", "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"},
        {"title": "ซีรีส์ตัวอย่าง 2", "url": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4"}
    ]
    for item in urls:
        list_item = xbmcgui.ListItem(label=item["title"])
        list_item.setInfo("video", {"title": item["title"]})
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=item["url"], listitem=list_item, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

if __name__ == '__main__':
    list_series()
