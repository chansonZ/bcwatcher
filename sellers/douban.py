import re
import requests

class DouBan():

    def __init__(self, book_name, book_id):
        self.name = 'douban'
        self.book_name = book_name
        self.book_id = book_id

    def query(self):
        # https://book.douban.com/subject/26802084/collections
        url = 'https://book.douban.com/subject/' + self.book_id + '/collections'
        html = requests.get(url).text
        return {
            'seller_name': self.name,
            'book_name': self.book_name,
            'book_id': self.book_id,
            'comment_count': self.find_comment_count(html),
            'latest_comment': self.find_latest_comment(html),
            'latest_star': self.find_latest_star(html)
        }

    # <span class="">n人参与评价</span>
    def find_comment_count(self, html):
        pattern = '(\d+)人参与评价'
        return re.search(pattern, html).group(1)

    # <p class="">xxx</p>
    def find_latest_comment(self, html):
        tag_begin = '<p class="">'
        tag_end = '</p>'
        idx_begin = html.index('<span class="allstar')
        idx_begin = html.index(tag_begin, idx_begin) + len(tag_begin)
        idx_end = html.index(tag_end, idx_begin)
        return html[idx_begin:idx_end].strip()

    # <span class="allstar??" title="xx"></span>
    def find_latest_star(self, html):
        pattern = '<span class="allstar(\d)\d"'
        return re.search(pattern, html).group(1)
