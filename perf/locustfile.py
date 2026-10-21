from locust import HttpUser, task, between
class ApiUser(HttpUser):
    host = 'http://127.0.0.1:5000'
    wait_time = between(0.1, 0.5)
    @task(2)
    def fast(self):
        self.client.get("/fast")

    @task(1)
    def user(self):
        self.client.get("/user/1")