import json
import os
import time


def get_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    return parent_dir


# 로그
def log(type_, content, filename='log.json'):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('[]')

    with open(filename, 'r+') as f:
        data = json.load(f)
        data.append({type_: [time.time(), content]})
        f.seek(0)
        json.dump(data, f)
