import requests

class JD():

    def __init__(self, book_name, book_id):
        self.name = 'jd'
        self.book_name = book_name
        self.book_id = book_id

    def query(self):
        # http://sclub.jd.com/productpage/p-11935272-s-0-t-3-p-0.html
        url = 'http://sclub.jd.com/productpage/p-' + self.book_id + '-s-0-t-3-p-0.html'
        json = requests.get(url).json(encoding='gbk')
        return {
            'seller_name': self.name,
            'book_name': self.book_name,
            'book_id': self.book_id,
            'comment_count': json['productCommentSummary']['commentCount'],
            'latest_comment': json['comments'][0]['content'],
            'latest_star': json['comments'][0]['score']
        }
