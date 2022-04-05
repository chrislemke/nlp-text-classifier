# -*- coding: utf-8 -*-

from ruakspider.cleaner import clean_up
from ruakspider.cleaner import title_clean_up
from ruakspider.cleaner import wiki_clean_up
from bs4 import BeautifulSoup
import scrapy
import os
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

BANNED = ["List", "Category", "Portal", "ISBN-Search"]

PATH = os.path.abspath(__file__ + f"/../../../loaded")


class WikiENSpider(CrawlSpider):
    name = "wikienspider"
    allowed_domains = ["en.wikipedia.org", "en.wikibooks.org", "en.wikisource.org"]
    link_extractor = LinkExtractor(
        deny=r"(:).*\1{1}",
        unique=True,
    )
    rules = [Rule(link_extractor, callback="parse_item", follow=True)]

    def parse_item(self, response):

        title = response.xpath("// title/text()").get()
        if self.exclude(title):
            return
        title = title_clean_up(title)

        soup = BeautifulSoup(response.body, features="lxml")

        for tag in soup.find_all("span"):
            tag.replaceWith("")

        for tag in soup.find_all("a", {"class": "notes"}):
            tag.replaceWith("")

        for tag in soup.find_all("sup"):
            tag.replaceWith("")

        for tag in soup.find_all("blockquote"):
            tag.replaceWith("")

        text = ""
        for content in soup.find_all("p"):
            text += f"{content.text}"

        text = clean_up(text)

        with open(
            f"{PATH}/en_wiki_{title.lower()}.txt", "a", encoding="UTF-8"
        ) as outfile:
            outfile.write(f"{text} ")
        outfile.close()

    def exclude(self, title):
        if [ele for ele in BANNED if (ele in title)]:
            return True
        else:
            False

    start_urls = [
        "https://en.wikipedia.org/wiki/Portal:Philosophy",
        "https://en.wikipedia.org/wiki/Wikipedia:Contents/Religion_and_belief_systems",
    ]
