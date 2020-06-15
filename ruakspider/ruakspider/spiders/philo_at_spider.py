# -*- coding: utf-8 -*-

import os
import scrapy
import io
from ruakspider.cleaner import clean_up
from ruakspider.cleaner import philo_at_clean_up
from scrapy.http import Request

FILE_STORE = os.path.abspath(
    __file__ + f"/../../../loaded")

FILE_LIST = os.path.abspath(
    __file__ + f"/../../url_phil_at_list.txt")


def list_from_file():
    urls = set()
    with open(FILE_LIST, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace('\n', '')
            urls.update([line])
    file.close()
    return list(urls)


class PhiloATSpider(scrapy.Spider):

    name = 'philoatspider'
    start_urls = list_from_file()

    def parse(self, response):
        href = response.xpath(
            "//a[starts-with(text(),'Download')]/@href").extract_first()
        yield Request(
            url=response.urljoin(href),
            callback=self.save
        )

    def save(self, response):
        path = response.url.split('/')[-1]
        if path.endswith('.pdf'):
            with open(f'{FILE_STORE}/{path}', 'wb') as file:
                file.write(response.body)
                print('')
