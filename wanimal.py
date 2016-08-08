import requests
import urllib
import re
import os.path
import time
import socket
from urllib2 import URLError


def add_image_url_to_wait_list(image_url):
    if image_url not in waitList:
        waitList.append(image_url)
        print image_url + " added to waitList[" + str(waitList.__len__()) + "]"


def remove_image_url_from_wait_list(image_url):
    if image_url in waitList:
        waitList.remove(image_url)
        print image_url + " removed from waitList[" + str(waitList.__len__()) + "]"


def add_image_url_to_saved_list(image_url):
    if image_url not in cacheList:
        cacheList.append(image_url)
        print image_url + " added to cacheList[" + str(cacheList.__len__()) + "]"
        remove_image_url_from_wait_list(image_url)


def download_image_array(image_array=[]):
    for m in image_array:
        image_url = m[m.rfind("http"):]
        image_name = image_url[image_url.rfind("/") + 1:]
        if image_url not in cacheList:
            image_path = savePath + image_name
            temp_path = image_path + ".tmp"
            if os.path.exists(image_path):
                add_image_url_to_saved_list(image_url)
                print image_name + " exists"
                continue
            try:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
                urllib.urlretrieve(image_url, temp_path)
                os.rename(temp_path, image_path)
                add_image_url_to_saved_list(image_url)
            except URLError, e:
                add_image_url_to_wait_list(image_url)
                print image_url + " download error\n" + e.message
                print "Sleep " + sleepTime + "s"
                time.sleep(sleepTime)
                print "Waked to work :)"
            except Exception, e:
                if os.path.isfile(temp_path):
                    os.remove(temp_path)
                add_image_url_to_wait_list(image_url)
                print image_url + " download exception: " + e.message
        else:
            print image_name + " repeated"


socket.setdefaulttimeout(15)
page = "http://wanimal1983.org/page/"
index = 0
savePath = 'E:/bain/wanimal/'
sleepTime = 5
cacheList = []
waitList = []
waitMaxLength = 10

while True:

    if waitList.__len__() > waitMaxLength:
        waitMaxLength += 10
        download_image_array(waitList)
    elif waitList.__len__() < waitMaxLength - 10:
        waitMaxLength -= 10

    index += 1
    pageUrl = page + str(index)
    # if index == 2:
    #     break

    print "Page " + str(index) + " collecting ..."

    result = requests.get(pageUrl)

    image_url_array = re.findall('http.*?1280\.(?:jpg|jpeg|png)', result.content)
    if image_url_array.__len__() == 0:
        break
    download_image_array(image_url_array)

while waitList.__len__() > 0:
    download_image_array(waitList)
