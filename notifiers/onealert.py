import json
import requests

# http://www.onealert.com/
class OneAlert:

    def __init__(self, app_key):
        self.app_key = app_key
        pass

    def summary(self, book_info):
        return '{seller}/{book}/{cc}/{star}*'.format(
            seller=book_info['seller_name'],
            book=book_info['book_name'],
            cc=book_info['comment_count'],
            star=book_info['latest_star']
        )

    def event_id(self, book_info):
        return '{book}:{cc}'.format(
            book=book_info['book_id'],
            cc=book_info['comment_count']
        )

    def notify(self, book_info):
        summary = self.summary(book_info)
        event_id = self.event_id(book_info)
        api = 'http://api.110monitor.com/alert/api/event'
        data = {
            'app': self.app_key,
            'eventId':  event_id,
            'eventType': 'trigger',
            'alarmName': summary,
            'entityName': summary,
            'priority': 1,
            'alarmContent': book_info['latest_comment']
        }
        # print(data)
        r = requests.post(api, json.dumps(data))
        return r.json()
