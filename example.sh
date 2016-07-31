#!/bin/bash
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