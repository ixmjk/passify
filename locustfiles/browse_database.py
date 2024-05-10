import random
import string

from locust import HttpUser, between, task

SEED_FILE = "custom_commands/management/commands/users.sql"


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        self.authenticate()

    def authenticate(self):
        response = self.client.post(
            "/auth/jwt/create/",
            json={
                "email": self.pick_random_email(),
                "password": "123",
            },
        )

        if response.status_code == 200:
            access_token = response.json().get("access")
            self.client.headers = {
                "Authorization": f"JWT {access_token}",
            }
            self.client.entry_ids = []

        print(f"[{response.status_code}] authenticate")

    def pick_random_email(self):
        with open(SEED_FILE, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            random_index = random.randint(0, line_count - 1)
            selected_line = lines[random_index].strip()
            selected_email = selected_line.split(" ")[16][1:-2]  # pick the email

        return selected_email

    def generate_random_string(self, min_len=10, max_len=20):
        characters = string.ascii_letters + string.digits
        length = random.randint(min_len, max_len)
        random_string = "".join(random.choice(characters) for _ in range(length))
        return random_string

    @task(4)
    def view_entry_list(self):
        response = self.client.get(
            "/my/database/",
        )
        print(f"[{response.status_code}] view_entry_list")

    @task(2)
    def add_entry(self):
        response = self.client.post(
            "/my/database/",
            json={
                "title": self.generate_random_string(),
                "username": self.generate_random_string(),
                "password": self.generate_random_string(),
                "url": f"http://{self.generate_random_string()}.com/",
                "notes": self.generate_random_string(),
            },
        )
        if response.status_code == 201:
            self.client.entry_ids.append(response.json().get("id"))
        print(f"[{response.status_code}] add_entry")

    @task(1)
    def view_entry(self):
        if self.client.entry_ids:
            response = self.client.get(
                f"/my/database/{random.choice(self.client.entry_ids)}/",
                name="/my/database/:id/",
            )
            print(f"[{response.status_code}] view_entry")

    @task(1)
    def update_entry(self):
        if self.client.entry_ids:
            response = self.client.put(
                f"/my/database/{random.choice(self.client.entry_ids)}/",
                name="/my/database/:id/",
                json={
                    "title": self.generate_random_string(),
                    "username": self.generate_random_string(),
                    "password": self.generate_random_string(),
                    "url": f"http://{self.generate_random_string()}.com/",
                    "notes": self.generate_random_string(),
                },
            )
            print(f"[{response.status_code}] update_entry")

    @task(1)
    def partial_update_entry(self):
        if self.client.entry_ids:
            response = self.client.patch(
                f"/my/database/{random.choice(self.client.entry_ids)}/",
                name="/my/database/:id/",
                json={
                    "username": self.generate_random_string(),
                    "password": self.generate_random_string(),
                },
            )
            print(f"[{response.status_code}] partial_update_entry")

    @task(1)
    def delete_entry(self):
        if self.client.entry_ids:
            entry_id = random.choice(self.client.entry_ids)
            response = self.client.delete(
                f"/my/database/{entry_id}/",
                name="/my/database/:id/",
            )
            if response.status_code == 204:
                self.client.entry_ids.remove(entry_id)
            print(f"[{response.status_code}] delete_entry")
