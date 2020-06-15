# -*- coding: utf-8 -*-

from ruakpider.cleaner import wiki_title_clean_up
from ruakspider.cleaner import wiki_clean_up
from bs4 import BeautifulSoup
import scrapy
import os
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

BANNED = [
    'Liste', 'Kategorie', 'Portal', 'Philosophiepreis‎', 'Institution', 'Arbeitsmittel', 'Philosophiezeitschrift', 'Phil.Cologne',
    'Das Philosophische Quartett', 'ISBN-Suche', 'Spezialseite', 'Category'
]

PATH = os.path.abspath(
    __file__ + f"/../../../loaded")


class WikiDESpider(CrawlSpider):
    name = 'wikidespider'
    allowed_domains = ['de.wikipedia.org',
                       'de.wikibooks.org', 'de.wikisource.org']
    link_extractor = LinkExtractor(
        deny=r'(:).*\1{1}',
        unique=True,
    )
    rules = [Rule(link_extractor, callback='parse_item', follow=False)]

    outfile = open(f'{PATH}/_wiki_TEST.txt', 'a', encoding='UTF-8')

    def parse_item(self, response):

        title = response.xpath('// title/text()').get()
        if self.exclude(title):
            print(f'IGNORED: {title}.')
            return
        title = wiki_title_clean_up(title)
        print(title)

        soup = BeautifulSoup(response.body, features="lxml")

        for tag in soup.find_all('span'):
            tag.replaceWith('')

        for tag in soup.find_all('a', {'class': 'notes'}):
            tag.replaceWith('')

        for tag in soup.find_all('sup'):
            tag.replaceWith('')

        for tag in soup.find_all('blockquote'):
            tag.replaceWith('')

        text = ""
        for content in soup.find_all('p'):
            text += f'{content.text}'

        text = wiki_clean_up(text)

        self.outfile.write(f'{text}\n')

    def exclude(self, title):
        if [ele for ele in BANNED if(ele in title)]:
            return True
        else:
            False

    start_urls = [
        'https://de.wikipedia.org/wiki/Kategorie:Philosophie'
    ]
