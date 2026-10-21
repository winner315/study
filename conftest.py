from common.logger import  get_logger
import pytest

from api.posts_api import PostsAPI
from login_data_result.api_client import ApiClient

@pytest.fixture()
def client():
    # print('前置\n')
    get_logger().info('conftest前置')
    yield ApiClient()
    # print('\n后置')
    get_logger().info('log:后置\n')

@pytest.fixture()
def post_api(client):
    return PostsAPI(client)