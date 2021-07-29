import csv


class Articles:

    def __init__(self, headline, page_url):
        super().__init__()
        self.headline = headline
        self.page_url = page_url

    def write_article(self):
        with open('articles.csv', 'a') as articles:
            data = [self.headline, self.page_url]
            writer = csv.writer(articles)
            writer.writerow(data)
