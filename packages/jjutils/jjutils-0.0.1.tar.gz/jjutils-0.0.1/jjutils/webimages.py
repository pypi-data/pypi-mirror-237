"""
Retrieves all images from a url

"""


import re
import sys
import time
from os.path import basename
from posixpath import basename

import urllib2
from urlparse import urlsplit


def process_url(raw_url):
    "processing the url string"
    if " " not in raw_url[-1]:
        raw_url = raw_url.replace(" ", "%20")
        return raw_url
    elif " " in raw_url[-1]:
        raw_url = raw_url[:-1]
        raw_url = raw_url.replace(" ", "%20")
        return raw_url


def get_images(url):
    "retrieves the images from the url"
    urlcontent = urllib2.urlopen(url).read()
    imgurls = re.findall('img .*?src="(.*?)"', urlcontent)
    time.sleep(1)
    for imgurl in imgurls:
        print(f"INFO: url = {imgurl}")

        try:
            time.sleep(1)
            imgurl = process_url(imgurl)
            imgdata = urllib2.urlopen(imgurl).read()
            filname = basename(urlsplit(imgurl)[2])
            output = open(filname, "wb")
            output.write(imgdata)
            output.close()
        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":
    url = sys.argv[1]
    get_images(url)
    # images_to_gcs()
