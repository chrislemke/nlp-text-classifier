# -*- coding: utf-8 -*-

from ruakspider.cleaner import wiki_title_clean_up
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
    __file__ + f"/../../../loaded/Politische Philosophie")


class WikiDESpider(CrawlSpider):
    name = 'wikidespider'
    allowed_domains = ['de.wikipedia.org',
                       'de.wikibooks.org', 'de.wikisource.org']
    link_extractor = LinkExtractor(
        deny=r'(:).*\1{1}',
        unique=True,
    )
    rules = [Rule(link_extractor, callback='parse_item', follow=False)]

    def parse_item(self, response):
        title = response.xpath('// title/text()').get()
        outfile = open(f'{PATH}/{title}.txt', 'a', encoding='UTF-8')
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

        outfile.write(f'{text}\n')

    def exclude(self, title):
        if [ele for ele in BANNED if(ele in title)]:
            return True
        else:
            False

    start_urls = [
        # 'https://de.wikipedia.org/wiki/Kategorie:Metaphysik',
        # 'https://de.wikipedia.org/wiki/Kategorie:Nat % C3 % BCrliche_Theologie',
        # 'https://de.wikipedia.org/wiki/Kategorie:Okkasionalismus',
        # 'https://de.wikipedia.org/wiki/Kategorie:Ontologie',
        # 'https://de.wikipedia.org/wiki/Kategorie:Dualismus',
        # 'https://de.wikipedia.org/wiki/Kategorie:Traditionalismus_(Philosophie)'

        # 'https://de.wikipedia.org/wiki/Kategorie:Ethik_(Philosophie)',
        # 'https://de.wikipedia.org/wiki/Kategorie:Moralphilosoph',
        # 'https://de.wikipedia.org/wiki/Kategorie:Bioethiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Christlicher_Sozialethiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Medizinethiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Umweltethiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Utilitarist',
        # 'https://de.wikipedia.org/wiki/Kategorie:Vertreter_der_Diskurstheorie',
        # 'https://de.wikipedia.org/wiki/Kategorie:Wirtschaftsethiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Ethische_Theorie',
        # 'https://de.wikipedia.org/wiki/Kategorie:Ethisches_Prinzip',
        # 'https://de.wikipedia.org/wiki/Kategorie:Metaethik'

        # 'https://de.wikipedia.org/wiki/Kategorie:Erkenntnistheorie',
        # 'https://de.wikipedia.org/wiki/Kategorie:Erkenntnistheoretiker',
        # 'https://de.wikipedia.org/wiki/Kategorie:Kantianismus',
        # 'https://de.wikipedia.org/wiki/Kategorie:Kantianer',
        # 'https://de.wikipedia.org/wiki/Kategorie:Neukantianer',
        # 'https://de.wikipedia.org/wiki/Kategorie:Wahrheit_(Philosophie)',
        # 'https://de.wikipedia.org/wiki/Kategorie:Wissen_(Philosophie)',
        # 'https://de.wikipedia.org/w/index.php?title=Kategorie:Erkenntnistheorie&pagefrom=Methodischer+Zweifel#mw-pages'

        'https://de.wikipedia.org/wiki/Kategorie:Politische_Philosophie',
        'https://de.wikipedia.org/wiki/Kategorie:Politischer_Philosoph',
        'https://de.wikipedia.org/wiki/Kategorie:Staatsphilosophie',
        'https://de.wikipedia.org/wiki/Kategorie:Staatstheorie',
        'https://de.wikipedia.org/wiki/Kategorie:Werk_der_Politischen_Philosophie'
    ]
