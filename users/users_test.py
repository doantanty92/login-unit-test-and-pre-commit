from django.test import TestCase
from rest_framework.test import APIClient


class AuthTest(TestCase):
    def register(self):
        client = APIClient()
        response = client.post(
            "/api/register",
            {
                "name": "Doan Tan Ty",
                "email": "doantanty@gmail.com",
                "password": "123456",
            },
        )
        self.assertEqual(response.status_code, 200)

    def login(self):
        self.client = APIClient()
        self.register()
        self.login_url = "/api/login"

        # Login successfully
        email = "doantanty@gmail.com"
        password = "123456"
        self.user_data = {"email": email, "password": password}
        res = self.client.post(self.login_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["user"].get("email"), email)
        self.assertIsNotNone(res.data["token"])

        # Login failed - user not found
        email = "doantanty1@gmail.com"
        password = "123456"
        self.user_data = {"email": email, "password": password}
        res = self.client.post(self.login_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data, "User not found!")

        # Login failed - wrong password
        email = "doantanty@gmail.com"
        password = "1234561"
        self.user_data = {"email": email, "password": password}
        res = self.client.post(self.login_url, self.user_data, format="json")

        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.data, "Incorrect password!")
