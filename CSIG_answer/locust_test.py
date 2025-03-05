from locust import HttpUser, task, between


class TestUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def test_api(self):
        self.client.get("/test", params={"a": 1, "b": "nihao"})