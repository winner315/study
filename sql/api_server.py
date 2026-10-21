from flask import Flask, request, jsonify
from sql.db_util import execute
from pymysql import IntegrityError

app = Flask(__name__)
@app.route('/employee', methods=['POST'])
def employee():
   try:
       d = request.get_json()
       execute("insert into employees(id,name,dept,salary) values (%s, %s, %s, %s)",
               (d['id'], d['name'], d['dept'], d['salary']))
   except IntegrityError:
       return jsonify({'code': 1, 'msg': 'id 已存在'}), 409
   return jsonify({'code': 0, 'msg': 'created', 'id': d['id']})
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, threaded=True)
