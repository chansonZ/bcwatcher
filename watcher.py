#!/usr/bin/python3

"""Book Comments Watcher.

Usage:
  watcher.py --books=<json> --notifiers=<json>
  watcher.py (-h | --help)
  watcher.py --version

Options:
  -h --help             Show this screen.
  --version             Show version.
  --books=<json>        Books JSON.
  --notifiers=<json>    Notifiers JSON.

"""

import json, os, tempfile
import requests
from docopt import docopt
from sellers.jd import JD
from sellers.dangdang import DangDang
from sellers.zcn import ZCN
from sellers.douban import DouBan
from notifiers.onealert import OneAlert

sellers_by_name = {
    'jd': JD,
    'z.cn': ZCN,
    'dangdang': DangDang,
    'douban': DouBan
}

def create_book(book_json):
    seller_name = book_json['seller']
    book_name = book_json['name']
    book_id = book_json['id']
    seller = sellers_by_name[seller_name]
    return seller(book_name, book_id)

def create_notifier(notifier_json):
    notifier_name = notifier_json['name']
    if notifier_name == 'onealert':
        app_key = notifier_json['app_key']
        return OneAlert(app_key)
    # todo

def load_comment_counts():
    tmp_file_path = os.path.join(tempfile.gettempdir(), 'bcw.json')
    if os.path.exists(tmp_file_path):
        return json.load(open(tmp_file_path, 'r'))
    else:
        return {}

def save_comment_counts(cc):
    tmp_file_path = os.path.join(tempfile.gettempdir(), 'bcw.json')
    json.dump(cc, open(tmp_file_path, 'w'))

def notify(notifiers, book_info):
    for notifier in notifiers:
        notifier.notify(book_info)

def watch(books, notifiers, cc_map):
    for book in books:
        book_info = book.query()
        new_cc = int(book_info['comment_count'])
        old_cc = cc_map.get(book.book_id, 0)
        cc_map[book.book_id] = new_cc
        if old_cc > 0 and new_cc > old_cc:
            notify(notifiers, book_info)
        else:
            print(new_cc)

args = docopt(__doc__, version='Book Comments Watcher 0.1')
books_json = json.loads(args['--books'])
notifiers_json = json.loads(args['--notifiers'])

books = [create_book(b) for b in books_json]
notifiers = [create_notifier(n) for n in notifiers_json]

comment_counts_map = load_comment_counts()
watch(books, notifiers, comment_counts_map)
save_comment_counts(comment_counts_map)
