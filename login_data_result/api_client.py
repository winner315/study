import logging
from common.logger import  get_logger
import requests


class ApiClient:
    def get(self,url: str, params=None ):
        try:
            resp = requests.get(url, params=params,timeout=30)
            if resp.status_code == 200:
                body = resp.json()
                get_logger().info('get请求成功')
                return body
            else:

                return None
        except Exception as e:
            get_logger().error(e)
            return None


