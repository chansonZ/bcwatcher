# bcwatcher
监控书评的小工具

# 运行环境
python(3.5+ & pip)
docopt(0.6.2+)
requests(2.10.0+)

# 测试
```sh
pip3 install docopt
pip3 install requests

python3 watcher.py \
  --books='[
    {"name": "自己动手写JVM", "seller": "jd",       "id": "11935272"  },
    {"name": "自己动手写JVM", "seller": "z.cn",     "id": "B01FX8YEKK"},
    {"name": "自己动手写JVM", "seller": "dangdang", "id": "23965877"  },
    {"name": "自己动手写JVM", "seller": "douban",   "id": "26802084"  }
  ]' \
  --notifiers='[
    {"name": "onealert", "app_key": "f62f3f40-330a-98b5-d56c-xxxxxxxxxxxx"}
  ]'
```

# 备注
通知是用过onealert发送的
