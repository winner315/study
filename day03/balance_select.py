import os
import requests
import json

response = requests.get(
    url="https://openrouter.ai/api/v1/key",
    headers={
        "Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}"
    },
)

data = response.json()                    # 先转成 Python 字典
daily_limit = data["data"]["limit_remaining"] # 注意是 daily_limit，不是 daliy_limit
print(f'剩余额度:\n{daily_limit}$')