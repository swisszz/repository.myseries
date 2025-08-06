# -*- coding: utf-8 -*-
import xbmcplugin, xbmcgui, xbmc
import sys, urllib.parse

addon_handle = int(sys.argv[1])
args = urllib.parse.parse_qs(sys.argv[2][1:])
mode = args.get('mode', [None])[0]

def open_url(name, url, icon):
    li = xbmcgui.ListItem(label=name)
    li.setArt({'thumb': icon, 'icon': icon, 'fanart': icon})
    li.setPath(url)
    li.setProperty("IsPlayable", "true")
    xbmcplugin.setResolvedUrl(addon_handle, True, li)

def list_main_menu():
    items = [
        {"label": "🎬 หนังใหม่ล่าสุด", "url": "https://my-series.com/category/movie/", "thumb": "https://my-series.com/wp-content/uploads/2024/03/johnwick4.jpg"},
        {"label": "📺 ละครไทย", "url": "https://my-series.com/category/thai-drama/", "thumb": "https://my-series.com/wp-content/uploads/2024/01/lakornthai.jpg"},
        {"label": "🇨🇳 ซีรีส์จีน", "url": "https://my-series.com/category/chinese-series/", "thumb": "https://my-series.com/wp-content/uploads/2025/07/nineyin2025_cover.jpg"},
        {"label": "🇰🇷 ซีรีส์เกาหลี", "url": "https://my-series.com/category/korean-series/", "thumb": "https://my-series.com/wp-content/uploads/2024/02/kdrama.jpg"},
        {"label": "⏪ รายการย้อนหลัง", "url": "https://my-series.com/category/vod/", "thumb": "https://my-series.com/wp-content/uploads/2024/02/throwback.jpg"},
        {"label": "📡 🇹🇭TV CHAK (ดูทีวีสด)", "url": "plugin://plugin.video.tvchak/?mode=live", "thumb": "https://n9.cl/y2z253"},
    ]
    for item in items:
        li = xbmcgui.ListItem(label=item['label'])
        li.setArt({'thumb': item['thumb'], 'icon': item['thumb'], 'fanart': item['thumb']})
        is_folder = item['url'].startswith("plugin://")
        xbmcplugin.addDirectoryItem(addon_handle, item['url'], li, isFolder=is_folder)
    xbmcplugin.endOfDirectory(addon_handle)

def list_live_tv():
    channels = [
        {"name": "CH7", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffac/7hd/7hd.m3u8", "logo": "https://n9.cl/4kmiht"},
        {"name": "Nation", "url": "https://nationtv-1jdcjo.cdn.byteark.com/fleetstream/nationtvlive/1080p/index.m3u8", "logo": "https://n9.cl/pkxl3"},
        {"name": "CH8", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffbe/ch8/ch8.m3u8", "logo": "https://n9.cl/d2ksaw"},
        {"name": "Nation CHAK", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffcc/nation/nation.m3u8", "logo": "https://n9.cl/r0we5"},
        {"name": "CH3 HD", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffae/3hd/3hd.m3u8", "logo": "https://n9.cl/9f0xf"},
        {"name": "TNN", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffdc/tnn/tnn.m3u8", "logo": "https://n9.cl/l869p"},
        {"name": "TPTV", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffec/tptv/tptv.m3u8", "logo": "https://n9.cl/b8u7i"},
        {"name": "Amarin HD", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffad/amarin/amarin.m3u8", "logo": "https://n9.cl/65b58o"},
        {"name": "Thairath HD", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffaf/thairath/thairath.m3u8", "logo": "https://n9.cl/409e5"},
        {"name": "Channel 8", "url": "https://cdn-th-vip.login.in.th:443/ch8/ch8/chunklist.m3u8", "logo": "https://n9.cl/3gdhl"},
        {"name": "Workpoint HD", "url": "https://global-media.sooplive.com/live/video/workpoint/1920x1080/playlist.m3u8", "logo": "https://n9.cl/dguzu"},
        {"name": "Workpoint", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffcb/workpoint/workpoint.m3u8", "logo": "https://n9.cl/dguzu"},
        {"name": "NBT", "url": "https://lb1-live-mv.v2h-cdn.com/hls/fffe/nbt/nbt.m3u8", "logo": "https://n9.cl/49yt5v"},
        {"name": "CH5", "url": "https://lb1-live-mv.v2h-cdn.com/hls/fffb/5hd/5hd.m3u8", "logo": "https://bit.ly/3aaooNF"},
        {"name": "Thai Chaiyo", "url": "https://live-iptv.thaichaiyo.tv/tcy/live-720P.m3u8", "logo": "https://n9.cl/y2z253"},
        {"name": "Looktung Network FM", "url": "http://vip.login.in.th:1935/looktungnetwork1/looktungnetwork1/playlist.m3u8", "logo": "https://n9.cl/q3t23i"},
        {"name": "Looktung LAKTHAI FM", "url": "http://radio11.plathong.net:8896/;stream.mp3", "logo": "https://n9.cl/dnycy"},
        {"name": "JKN", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffda/jkn18/jkn18.m3u8", "logo": "https://n9.cl/unxb8"},
        {"name": "Thai PBS", "url": "https://lb1-live-mv.v2h-cdn.com/hls/fffd/tpbs/tpbs.m3u8", "logo": "https://bit.ly/3R57wIK"},
        {"name": "T Sport", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffef/tsport/tsport.m3u8", "logo": "https://n9.cl/ry89h"},
        {"name": "Mono 29", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffbc/mono29/mono29.m3u8", "logo": "https://n9.cl/afnnk"},
        {"name": "Mcot", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffbb/mcot/mcot.m3u8", "logo": "https://n9.cl/83jvz"},
        {"name": "One", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffba/one/one.m3u8", "logo": "https://n9.cl/ipdj6"},
        {"name": "PPTV", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffab/pptv/pptv.m3u8", "logo": "https://n9.cl/wmbwp"},
        {"name": "GMM25 (Akamai)", "url": "https://bcovlive-a.akamaihd.net/57d4bf695e80436d9335f4f50adbe438/ap-southeast-1/6415628290001/7e85dc4a59904e45b4fdffebd62e1d82/playlist_ssaiM.m3u8", "logo": "https://n9.cl/adt8o"},
        {"name": "GMM25", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffbf/gmm25/gmm25.m3u8", "logo": "https://n9.cl/wmbwp"},
        {"name": "True 24", "url": "https://lb1-live-mv.v2h-cdn.com/hls/ffca/true24/true24.m3u8", "logo": "https://n9.cl/0ws87l"},
        {"name": "News 1", "url": "http://news1.live14.com/stream/news1.m3u8", "logo": "https://n9.cl/s9j3kg"},
        {"name": "Suwannabhumi", "url": "https://live.bangkokstream.com:19360/suwannabhumi/suwannabhumi.m3u8", "logo": "https://n9.cl/4nvv0"},
        {"name": "Police Channel", "url": "https://cdn-th-vip.livestreaming.in.th/policetv/policetv/playlist.m3u8", "logo": "https://n9.cl/baylk"},
    ]
    for ch in channels:
        li = xbmcgui.ListItem(label=ch["name"])
        li.setArt({'thumb': ch["logo"], 'icon': ch["logo"], 'fanart': ch["logo"]})
        li.setPath(ch["url"])
        li.setProperty("IsPlayable", "true")
        xbmcplugin.addDirectoryItem(addon_handle, ch["url"], li, isFolder=False)
    xbmcplugin.endOfDirectory(addon_handle)

if mode == "open":
    name = args.get("name", [""])[0]
    url = args.get("url", [""])[0]
    icon = args.get("icon", [""])[0]
    open_url(name, url, icon)
elif mode == "live":
    list_live_tv()
else:
    list_main_menu()
