#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmcplugin,xbmcaddon,xbmcgui,os,sys

addon = xbmcaddon.Addon()
home = addon.getAddonInfo('path').decode('utf-8')
xbmcplugin.setContent(handle=int(sys.argv[1]), content='songs')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
iconpath = xbmc.translatePath(home+"/icon/")

def add_item(url,infolabels,img='',fanart=''):
    listitem = xbmcgui.ListItem(infolabels['title'],iconImage=img,thumbnailImage=img)
    listitem.setInfo('audio',infolabels)
    listitem.setProperty('IsPlayable','true')
    listitem.setProperty('fanart_image',fanart)
    xbmcplugin.addDirectoryItem(int(sys.argv[1]),url,listitem)

add_item('http://meralunafm.radionetz.de:8000/meralunafm.mp3',{"title":'Mera Luna FM'},os.path.join(iconpath,'mlfm.png'),fanart)
add_item('http://www.schwarze-welle.de/play.m3u',{"title":'Radio Schwarze Welle'},os.path.join(iconpath,'swelle.png'),fanart)
add_item('http://178.33.32.217/stream/rjmvggsr.pls?mp=/stream',{"title":'Radio Dunkle Welle'},os.path.join(iconpath,'rdw.png'),fanart)
add_item('http://radio-hazzardofdarkness.de/infusions/gr_radiostatus_panel/gr_radiostatus_player.php?id=1&p=asx',{"title":'Radio Hazard of Darkness'},os.path.join(iconpath,'hod.png'),fanart)
add_item('http://stream.laut.fm/schattenreich',{"title":'Radio Schattenreich'},os.path.join(iconpath,'schatrei.png'),fanart)
add_item('http://stream.laut.fm/ultradarkradio',{"title":'UltraDarkRadio'},os.path.join(iconpath,'udr.png'),fanart)
add_item('http://stream.laut.fm/schwarzlauscher',{"title":'Schwarzlauscher'},os.path.join(iconpath,'schwlau.png'),fanart)
add_item('http://darkclubradio.stream.laut.fm/darkclubradio?t302=2017-12-08_19-50-04&uuid=61e574ad-b344-4961-99b0-15a9b4ecf393',{"title":'DarkClubRadio'},os.path.join(iconpath,'dcr.png'),fanart)
add_item('http://5.196.64.74:5060/stream',{"title":'Deutschrock Lounge'},os.path.join(iconpath,'dlr.png'),fanart)
add_item('http://der-barde.stream.laut.fm/der-barde?t302=2017-12-08_19-57-15&uuid=6b93ad95-db68-4bb9-ad93-cd6755b353e0',{"title":'Der-Barde'},os.path.join(iconpath,'barde.png'),fanart)
add_item('http://radio.zwischen-welten.info:8000/listen/',{"title":'Zwischen-Welten Radio'},os.path.join(iconpath,'zwr.png'),fanart)
add_item('http://rabenwind.stream.laut.fm/rabenwind?ref=radiode&t302=2017-12-08_20-02-45&uuid=fcc3bbd7-02e5-48b9-a6f7-128d2e018300',{"title":'Radio Rabenwind'},os.path.join(iconpath,'rw.png'),fanart)

xbmc.executebuiltin('Container.SetViewMode(100)')
xbmcplugin.endOfDirectory(int(sys.argv[1]))
#darkstations