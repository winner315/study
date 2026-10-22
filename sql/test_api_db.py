import requests
import pytest
from sql.db_util import query,execute

BASE = 'http://127.0.0.1:5001'
TID = 9001

@pytest.fixture()
def emp():
    execute('delete from employees where id= %s',(TID,))
    yield TID
    execute('delete from employees where id= %s',(TID,))

def test_add_employee(emp):
    body = {"id":TID,"name":"qa_w5","dept":"qa","salary":100000}
    r = requests.post(BASE+'/employee',json=body)
    assert r.status_code == 200
    assert r.json()['code'] == 0

    rows = query('select * from employees where id= %s',(TID,))
    assert len(rows) == 1

    id,name,dept,salary = rows[0]
    assert salary == 99999