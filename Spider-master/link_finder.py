from html.parser import HTMLParser
from urllib import parse
from write_articles import Articles
from general import *


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        self.articles = set()
        self.title = False

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if tag == 'title' and self.page_url not in self.articles and self.page_url != self.base_url:
            self.title = True
            #one title from a page
            self.articles.add(self.page_url)
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    if '#' not in url:
                        self.links.add(url)

    def handle_data(self, data):
        if self.title and not data.isspace():
            article = Articles(data, self.page_url)
            article.write_article()
            self.title = False

    def page_links(self):
        return self.links

    def error(self, message):
        pass
