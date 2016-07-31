import re
import requests

class DangDang:

    def __init__(self, book_name, book_id):
        self.name = 'dangdang'
        self.book_name = book_name
        self.book_id = book_id

    def query(self):
        # http://comm.dangdang.com/reviewlist/23965877-1-0-2-1
        url = 'http://comm.dangdang.com/reviewlist/' + self.book_id + '-1-0-2-1'
        html = requests.get(url).text
        return {
            'seller_name': self.name,
            'book_name': self.book_name,
            'book_id': self.book_id,
            'comment_count': self.find_comment_count(html),
            'latest_comment': self.find_latest_comment(html),
            'latest_star': self.find_latest_star(html)
        }

    # 全部(n)
    def find_comment_count(self, html):
        pattern = '全部\((\d+)\)'
        return re.search(pattern, html).group(1)

    # <p class="re_content">xxx</p>
    def find_latest_comment(self, html):
        pattern = '<p class="re_content">(.*)</p>'
        return re.search(pattern, html).group(1)

    # <span class="star_icon star_static static_?"></span>
    def find_latest_star(self, html):
        pattern = '<span class="star_icon star_static static_(\d+)">'
        return re.search(pattern, html).group(1)
