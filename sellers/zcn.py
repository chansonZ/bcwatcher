import re
import requests

class ZCN():

    def __init__(self, book_name, book_id):
        self.name = 'z.cn'
        self.book_name = book_name
        self.book_id = book_id
        self.comment_count = 0

    def query(self):
        # https://www.amazon.cn/product-reviews/B01FX8YEKK/ref=cm_cr_dp_see_all_btm?ie=UTF8&showViewpoints=1&sortBy=recent
        url = 'https://www.amazon.cn/product-reviews/' + self.book_id + '/ref=cm_cr_dp_see_all_btm?ie=UTF8&showViewpoints=1&sortBy=recent'
        html = requests.get(url).text
        return {
            'seller_name': self.name,
            'book_name': self.book_name,
            'book_id': self.book_id,
            'comment_count': self.find_comment_count(html),
            'latest_comment': self.find_latest_comment(html),
            'latest_star': self.find_latest_star(html)
        }

    # <span class="a-size-medium totalReviewCount">n</span>
    def find_comment_count(self, html):
        pattern = '<span class="a-size-medium totalReviewCount">(\d+)</span>'
        return re.search(pattern, html).group(1)

    # <span class="a-size-base review-title a-text-bold">xxx</span>
    # <span class="a-size-base review-text">xxx</span>
    def find_latest_comment(self, html):
        pattern = '<span class="a-size-base review-text">([^<]*)</span>'
        return re.search(pattern, html).group(1)

    # <i class="a-icon a-icon-star a-star-? review-rating">
    def find_latest_star(self, html):
        pattern = '<i class="a-icon a-icon-star a-star-(\d+) review-rating">'
        return re.search(pattern, html).group(1)

