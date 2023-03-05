#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
from urllib.request import urlretrieve

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def create_html_file(dest_dir: str):
    """
    function receives path to directory file where images are and create there an html file to discover the photo.
    :param dest_dir:
    """
    file_in_directory_list = [name for name in os.listdir(dest_dir)]
    with open(os.path.join(dest_dir, 'index.html'), 'wt') as f:
        f.write('<html><body>\n')
        for i, name in enumerate(file_in_directory_list):
            if name[-4:] == '.jpg':
                f.write(f'<img src="img{i}.jpg">')
        f.write('\n</body></html>')
    print(f'Everything is ready :)\nopen the HTML file and discover the photo!!!\n(HTML file is at:{dest_dir} )')


def sort_url_key(url: str):
    """
    function is used to sort url by 2nd word if present
    """
    match = re.search(r'(\S+)-(\S+)\.jpg+', url)
    if match:
        return match.group(2)
    else:
        return url


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    try:
        with open(filename, 'r') as f:
            strings = sorted(list(set(re.findall(r'\S*puzzle\S*[.]jpg', f.read()))), key=sort_url_key)
    except BaseException as error:
        print('Error: at "read_urls" function ', error)
        sys.exit(1)
    else:
        host = filename[1+filename.index('_'):]
        return ['http://' + host + substring for substring in strings]


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    else:
        for file in os.listdir(dest_dir):
            if file[-4:] == '.jpg':
                os.remove(os.path.join(dest_dir, file))

    for index, url in enumerate(img_urls):
        try:
            img_file_name = os.path.join(dest_dir, f'img{index}.jpg')
            urlretrieve(url, img_file_name)
        except BaseException as error:
            print('Error: at "download_images" function. ', error)

    create_html_file(dest_dir)


################################################
## DO NOT EDIT THE CODE BELOW
################################################

def main():
    args = sys.argv[1:]

    if not args:
        print('Too few arguments! Usage: [--todir dir] logfile ')
        return

    todir = ''
    if args[0] == '--todir':
        if len(args) < 3:
            print('Too few arguments! Usage: [--todir dir] logfile ')
            return            
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
