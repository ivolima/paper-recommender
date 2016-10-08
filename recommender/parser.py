# -*- coding: utf-8 -*-

# Author: Ivo Romario <ivo.romario@gmail.com>
# License:

from bs4 import BeautifulSoup


class Parser(object):

    def __init__(self, doc_path):
        self.doc = BeautifulSoup(open(doc_path))

    def parse_title(self):
        return self.doc.find(id="article_title").text

    def parse_authors(self, join_authors=True):
        authors = self.doc.select("a.author")
        authors = [a.text for a in authors]

        if join_authors:
            authors = " ",join(authors)
        return authors

    def parse_abstract(self):
        return self.doc.find(id="blockquote").text

