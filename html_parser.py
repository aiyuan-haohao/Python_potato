#!/usr/bin/python
# -*- coding: UTF-8 -*-
#html解析器
# import re
# import urlparse
#
# from bs4 import BeautifulSoup
# class HtmlParser(object):
#
#     def parser(self, page_url, html_cont):
#         if page_url is None or html_cont is None:
#             return
#
#         soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
#         new_urls = self._get_new_urls(page_url, soup)
#         new_data = self._get_new_data(page_url, soup)
#
#         return new_urls,new_data
#
#     def _get_new_urls(self, page_url, soup):
#         new_urls = set()
#         #/view /123.htm
#         #https://baike.baidu.com/item/Python/407313?fr=aladdin#1
#         links = soup.find_all('a',href=re.compile(r"/item/"))
#         for link in links:
#             new_url = link['href']
#             new_full_url = urlparse.urljoin(page_url,new_url)
#             new_urls.add(new_full_url)
#         return new_urls
#     #解析数据
#     def _get_new_data(self, page_url, soup):
#         res_data = {}
#
#         #url
#         res_data['url'] = page_url
#
#
#         #<dd class="lemmaWgt-lemmaTitle-title"></dd>
#         title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('hi')
#         res_data['title'] = title_node.get_text()
#
#        #<div class="para" label-module="para">
#         summary_node = soup.find('div',class_="label-module")
#         res_data['summary'] = summary_node.get_text()
#         return res_data
import re
import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.htm
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data