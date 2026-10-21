from pathlib import Path

import yaml


def load_cases():
    path = Path(__file__).parent / "posts.yaml"
    ids = []
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        print(data)
        for post in data:
            ids.append(post["user_id"])
        print(ids)
    return ids
