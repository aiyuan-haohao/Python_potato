#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import urllib2
# #html下载器
# class HtmlDownloader(object):
#
#     def downloader(self, url):
#         if url is None:
#             return None
#
#         response = urllib2.urlopen(url)
#
#         if response.getcode() != 200:
#             return None
#
#         return response.read()
import urllib2


class HtmlDownloder(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()
