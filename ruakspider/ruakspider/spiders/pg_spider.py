# -*- coding: utf-8 -*-

from ruakspider.cleaner import clean_up
from ruakspider.cleaner import title_clean_up
from bs4 import BeautifulSoup
import re
import os
import scrapy
import codecs
import io

PATH = os.path.abspath(
    __file__ + f"/../../../loaded")


class PGSpider(scrapy.Spider):
    name = 'pgspider'

    def parse(self, response):
        author = response.url.split('/')[3]
        title = response.url.split('/')[4]
        author = title_clean_up(author)
        soup = BeautifulSoup(response.body, features="lxml")

        for tag in soup.find_all('span'):
            tag.replaceWith('')

        for tag in soup.find_all('a', {'class': 'notes'}):
            tag.replaceWith('')

        text = ""
        for content in soup.find_all('p'):
            text += f' {content.text}'

        text = clean_up(text)

        with open(f'{PATH}/_phil_{author.lower()}-{title.lower()}.txt', 'a', encoding='UTF-8') as outfile:
            outfile.write(f'{text} ')
        outfile.close()

        next_page = response.xpath(
            "//a[starts-with(text(),'weiter')]/@href").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    start_urls = [

        # Aristoteles
        # 'https://www.projekt-gutenberg.org/aristote/politik/chap002.html',
        # 'https://www.projekt-gutenberg.org/aristote/nikomach/niko0101.html',

        # Platon
        # 'https://www.projekt-gutenberg.org/platon/platowr1/platow1.html',
        # 'https://www.projekt-gutenberg.org/platon/platowr2/gorgias.html',
        'https://www.projekt-gutenberg.org/platon/platowr3/staat.html',

        # Hegel
        # 'https://www.projekt-gutenberg.org/hegel/phaenom/phaenom.html',
        # 'https://www.projekt-gutenberg.org/hegel/vorphilo/vorphilo.html',
        # 'https://www.projekt-gutenberg.org/hegel/logik1/chap001.html',
        # 'https://www.projekt-gutenberg.org/hegel/logik2/logik2.html',

        # Nietzsche
        # 'https://www.projekt-gutenberg.org/nietzsch/zara/als2001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/antichri/chap001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/willmac1/chap001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/willmac2/chap001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/wissensc/chap001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/tragoedi/chap001.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/eccehomo/chap002.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/jenseits/chap002.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/menschli/mensch01.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/menschl2/chap003.html',
        # 'https://www.projekt-gutenberg.org/nietzsch/genealog/geneal01.html',

        # Kant
        # 'https://www.projekt-gutenberg.org/kant/naturg/chap02.html',
        # 'https://www.projekt-gutenberg.org/kant/gefuehl/chap001.html',
        # 'https://www.projekt-gutenberg.org/kant/sitte/sitte.html',
        # 'https://www.projekt-gutenberg.org/kant/absicht/absicht.html',
        # 'https://www.projekt-gutenberg.org/kant/kritikpr/krtvor1.html',
        # 'https://www.projekt-gutenberg.org/kant/krvb/krvb001.html',
        # 'https://www.projekt-gutenberg.org/kant/kuk/kukvor1.html',
        # 'https://www.projekt-gutenberg.org/kant/prolegom/prolegom.html',
        # 'https://www.projekt-gutenberg.org/kant/streit/streit.html',
        # 'https://www.projekt-gutenberg.org/kant/deutlich/chap001.html',
        # 'https://www.projekt-gutenberg.org/kant/aufklae/aufkl001.html',
        # 'https://www.projekt-gutenberg.org/kant/ewfriede/chap001.htm',
        # 'https://www.projekt-gutenberg.org/kant/1grund/1grund.html',
        # 'https://www.projekt-gutenberg.org/kant/geisters/chap001.html',
        # 'https://www.projekt-gutenberg.org/kant/einricht/chap001.html',

        # Schopenhauer
        # 'https://www.projekt-gutenberg.org/schopenh/aphorism/chap003.html',
        # 'https://www.projekt-gutenberg.org/schopenh/weltwil1/chap001.html',
        # 'https://www.projekt-gutenberg.org/schopenh/weltwil2/chap001.html',
        # 'https://www.projekt-gutenberg.org/schopenh/eristik/eristik.html',

        # Descartes
        # 'https://www.projekt-gutenberg.org/descarte/grunphil/grunphil.html',

        # Spinoza
        # 'https://www.projekt-gutenberg.org/spinoza/ethik/chap002.html',

        # Kierkegaard
        # 'https://www.projekt-gutenberg.org/kierkega/selbstpr/chap003.html',

        # Hume
        # 'https://www.projekt-gutenberg.org/hume/dialoge/chap002.html',

        # Leibniz
        # 'https://www.projekt-gutenberg.org/leibniz/kl-schri/chap001.html',
        # 'https://www.projekt-gutenberg.org/leibniz/monaden/monaden.html',

        # Fichte
        # 'https://www.projekt-gutenberg.org/fichte/franzrev/franzrev.html',
        # 'https://www.projekt-gutenberg.org/fichte/seligleb/chap005.html',
        # 'https://www.projekt-gutenberg.org/fichte/bestimmu/chap004.html',
        # 'https://www.projekt-gutenberg.org/fichte/dnation/dnati01.html',

        # Schelling
        # 'https://www.projekt-gutenberg.org/schellin/philoffe/philoffe.html',
        # 'https://www.projekt-gutenberg.org/schellin/essays/natur.html',
        # 'https://www.projekt-gutenberg.org/schellin/ichprinz/chap003.html',
        # 'https://www.projekt-gutenberg.org/schellin/weltseel/chap003.html',

        # Feuerbach
        # 'https://www.projekt-gutenberg.org/feuerbal/wesenrel/wesenrel.html',
        # 'https://www.projekt-gutenberg.org/feuerbal/wesenchr/chap003.html',

        # Montaigne
        # 'https://www.projekt-gutenberg.org/montaign/essay/essay.html',

        # Schiller
        # 'https://www.projekt-gutenberg.org/schiller/anstalt/anstalt.html',
        # 'https://www.projekt-gutenberg.org/schiller/gemeine/gemeine.html',
        # 'https://www.projekt-gutenberg.org/schiller/phbriefe/phbriefe.html',
        # 'https://www.projekt-gutenberg.org/schiller/naivsent/naivsent.html',
        # 'https://www.projekt-gutenberg.org/schiller/anmutwde/anmutwde.html',
        # 'https://www.projekt-gutenberg.org/schiller/erhaben/erhaben.html',
        # 'https://www.projekt-gutenberg.org/schiller/pathos/pathos.html',
        # 'https://www.projekt-gutenberg.org/schiller/traggegn/traggegn.html',
        # 'https://www.projekt-gutenberg.org/schiller/mornutz/mornutz.html',
        # 'https://www.projekt-gutenberg.org/schiller/tierisch/tierisch.html',
        # 'https://www.projekt-gutenberg.org/schiller/aesterz/aesterz.html',
        # 'https://www.projekt-gutenberg.org/schiller/grformen/grformen.html',
        # 'https://www.projekt-gutenberg.org/schiller/trkunst/trkunst.html',
        # 'https://www.projekt-gutenberg.org/schiller/vaesthet/vaesthet.html',

        # Goethe
        # 'https://www.projekt-gutenberg.org/goethe/dichwah1/chap001.html',
        # 'https://www.projekt-gutenberg.org/goethe/dichwah2/chap001.html',
        # 'https://www.projekt-gutenberg.org/goethe/werther/werther.html',
        # 'https://www.projekt-gutenberg.org/goethe/italien/ital111.html',
        # 'https://www.projekt-gutenberg.org/goethe/naturwi1/chap02.html',
        # 'https://www.projekt-gutenberg.org/goethe/nat92-97/nat92-97.html',

        # Rousseau
        # 'https://www.projekt-gutenberg.org/rousseau/gesellsc/chap001.html',
        # 'https://www.projekt-gutenberg.org/rousseau/emil1/emil1.html',
        # 'https://www.projekt-gutenberg.org/rousseau/emil2/emil2.html',
        # 'https://www.projekt-gutenberg.org/rousseau/bekennt1/bekennt1.html',
        # 'https://www.projekt-gutenberg.org/rousseau/bekennt2/bekennt2.html',

        # Bacon
        # 'https://www.projekt-gutenberg.org/bacon/organon/chap002.html',

        # Mauthner
        # 'https://www.projekt-gutenberg.org/mauthner/phil-bd1/phil-bd1.html',
        # 'https://www.projekt-gutenberg.org/mauthner/phil-bd2/chap001.html',

        # Vorländer
        # 'https://www.projekt-gutenberg.org/vorlaend/volkphil/chap002.html',

        # Machiavelli
        # 'https://www.projekt-gutenberg.org/machiave/fuerst/chap001.html',
        # 'https://www.projekt-gutenberg.org/machiave/mensstaa/chap001.html',

        # Marx
        # 'https://www.projekt-gutenberg.org/marx/elendphi/chap002.html',
        # 'https://www.projekt-gutenberg.org/marx/heilgfam/chap002.html',
        # 'https://www.projekt-gutenberg.org/marx/lohnprei/chap001.html',
        # 'https://www.projekt-gutenberg.org/marx/manifest/manifest.html',

        # Benjamin
        # 'https://www.projekt-gutenberg.org/benjamin/bauduebe/chap01.html',
        # 'https://www.projekt-gutenberg.org/benjamin/menschen/chap003.html',
        # 'https://www.projekt-gutenberg.org/benjamin/deuroman/chap01.html',
        # 'https://www.projekt-gutenberg.org/benjamin/sprache/chap01.html',

        # Erasmus
        'https://www.projekt-gutenberg.org/erasmus/torheit/torheit.html',
        # 'https://www.projekt-gutenberg.org/erasmus/gespraec/chap001.html',

        # Freud
        # 'https://www.projekt-gutenberg.org/freud/ichundes/ichundes.html',
        # 'https://www.projekt-gutenberg.org/freud/unbehag/unbehag.html',
        # 'https://www.projekt-gutenberg.org/freud/endlich/endlich.html',
        # 'https://www.projekt-gutenberg.org/freud/analyse/analyse.html',
        # 'https://www.projekt-gutenberg.org/freud/illusion/illusion.html',

        # Herder
        # 'https://www.projekt-gutenberg.org/herder/sprache/sprach01.html',

        # Konfuzius
        # 'https://www.projekt-gutenberg.org/konfuziu/gespraec/chap001.html',

        # Laozi
        # 'https://www.projekt-gutenberg.org/laotse/taotekin/chap002.html',

        # Montesquieu
        'https://www.projekt-gutenberg.org/montesqu/schrifte/chap002.html',

        # More
        # 'https://www.projekt-gutenberg.org/morus/utopia/chap001.html',

        # Simmel
        # 'https://www.projekt-gutenberg.org/simmel/philkuns/chap001.html',
        # 'https://www.projekt-gutenberg.org/simmel/socidiff/chap001.html',
        # 'https://www.projekt-gutenberg.org/simmel/schoniet/schoniet.html',
        'https://www.projekt-gutenberg.org/simmel/philgeld/philgeld.html',
        # 'https://www.projekt-gutenberg.org/simmel/philmode/philmode.html',

        # Spengler
        # 'https://www.projekt-gutenberg.org/spengler/jahrents/chap001.html',
        # 'https://www.projekt-gutenberg.org/spengler/preussoz/preussoz.html',
        # 'https://www.projekt-gutenberg.org/spengler/unterga1/chap003.html',
        # 'https://www.projekt-gutenberg.org/spengler/unterga2/unterga2.html',

        # Xenophon
        # 'https://www.projekt-gutenberg.org/xenophon/anabasis/vol01chap001.html',
        # 'https://www.projekt-gutenberg.org/xenophon/kyropaed/preface.html',
        # 'https://www.projekt-gutenberg.org/xenophon/sokrates/sokrat01.html',
        # 'https://www.projekt-gutenberg.org/xenophon/gastmahl/gastmavb.html'
    ]
