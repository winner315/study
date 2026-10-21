import pytest

def test_get(client):
    resp = client.get('https://jsonplaceholder.typicode.com/posts/1')
    print(resp)
    assert resp is not None
    assert resp['id'] == 1
def test_post(client):
    resp = client.get('https://jsonplaceholder.typicode.com/posts/',
                       params={'userId':1,'_limit':5})
    assert resp is not None
    assert len(resp) ==5

@pytest.mark.parametrize('user_Id',[1,2,3])
def test_post03(client,user_Id):
    resp = client.get('https://jsonplaceholder.typicode.com/posts/',
                       params={'userId':user_Id})
    assert resp is not None
    for posts in resp:
        assert posts['userId'] == user_Id


def test_post04(client):
    resp = client.get('https://jsonplom/posts/')
    assert resp is  None

