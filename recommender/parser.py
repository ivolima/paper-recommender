# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

from bs4 import BeautifulSoup


class Parser(object):

    def __init__(self, doc_path):
        self.__doc = BeautifulSoup(open(doc_path))
        #self.html = self.__doc.html

    def parse_title(self):
        title = unicode(self.__doc.find(id="article_title").text)
        return title.encode('utf-8').strip()

    def parse_authors(self, join_authors=True):
        authors = self.__doc.select("a.author")
        if authors:
            authors = [unicode(a.text) for a in authors]
            if join_authors:
                authors = u" ".join(authors).encode('utf-8').strip()
            return authors
        return ""

    def parse_abstract(self):
        abstract = self.__doc.select("#abstract-body")
        if abstract:
            return abstract[0].text.encode('utf-8').strip()
        return ""
        #return self.__doc.find(id="abstract-body").text

