#!/usr/bin/env python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import urllib2
import time
import sys
import os

artist_name = sys.argv[1]
artist_url_name = urllib.quote(artist_name.decode(sys.stdin.encoding).encode('utf-8'))

album_name = sys.argv[2]
album_url_name = urllib.quote(album_name.decode(sys.stdin.encoding).encode('utf-8'))

def xiami():
    global artist_url_name
    global album_url_name
    xiami_album_search_url = 'http://www.xiami.com/search/album?key=' + artist_url_name + '+' + album_url_name
    try:
        search_result_object = pq(url=xiami_album_search_url)
        album_info_element = search_result_object('div.albumBlock_list div.album_item100_block p.cover a.CDcover100')
        album_info_url = 'http://www.xiami.com' + album_info_element.attr('href')
        album_info_object = pq(url=album_info_url)
        album_picture_element = album_info_object('a#cover_lightbox')
        album_picture_url = album_picture_element.attr('href').encode('utf-8', 'ignore')
        return album_picture_url
    except Exception, e:
        raise

def ting():
    global artist_url_name
    global album_url_name
    ting_album_search_url = 'http://ting.baidu.com/search?key=' + artist_url_name + '+' + album_url_name
    try:
        search_result_object = pq(url=ting_album_search_url)
        album_info_element = search_result_object.find('div.song-item').eq(0).find('span.album-title a')
        album_info_url = 'http://ting.baidu.com' + album_info_element.attr('href')
        album_info_object = pq(url=album_info_url)
        album_picture_element = album_info_object('div.album-cover img')
        album_picture_url = 'http:' + album_picture_element.attr('src').encode('utf-8', 'ignore')
        return album_picture_url
    except Exception, e:
        raise

def main():
    try:
        picture_url = xiami()
    except Exception, e:
        try:
            picture_url = ting()
        except Exception, e:
            #xiami and ting can not worked, i can do nothing for this
            return -1
    print picture_url
if __name__ == '__main__':
    main()
