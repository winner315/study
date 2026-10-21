import pytest
import allure
from data.rd import load_cases

from common.assert_util import assert_ok


# post_api 夹具已在 study/conftest.py 里定义（返回 PostsAPI(client)），此处无需重复定义

@allure.feature('posts接口')
@allure.story('按照用户id查询')
@allure.title('查询用户id{user_id}的帖子')
@pytest.mark.parametrize("user_id", load_cases())
def test_posts(post_api, user_id):
    resp = post_api.get_posts_by_user(user_id)   # 调用接口层方法，用例里不出现 URL
    assert_ok(resp)
    for post in resp:
        assert post['userId'] == user_id


