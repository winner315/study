from flask import Flask, jsonify
import time, random

app = Flask(__name__)

@app.route("/fast")
def fast():
    return jsonify({"msg": "ok", "code": 0})

@app.route("/slow")
def slow():
    time.sleep(1)
    return jsonify({"msg": "slow", "code": 0})

@app.route("/random")
def random_api():
    time.sleep(random.uniform(0, 0.3))              # ① 随机延迟 → RT 波动
    if random.random() < 0.2:                        # ② 20% 概率失败 → 错误率
        return jsonify({"msg": "server error", "code": 500}), 500
    return jsonify({"msg": "ok", "code": 0})

@app.route("/cpu")
def cpu():
    x = 0
    for i in range(3_000_000):                        # ③ CPU 密集 → 瓶颈
        x += i * i
    return jsonify({"msg": "cpu done", "code": 0, "x": x})

@app.route("/user/<int:uid>")
def user(uid):
    return jsonify({"code": 0, "uid": uid})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, threaded=True)