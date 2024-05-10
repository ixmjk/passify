import os
import subprocess
import sys
import time

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs the project (use it for development!)."

    def handle(self, *args, **options):
        self.run_docker_compose_up()
        time.sleep(10)
        self.start_celery_worker()
        time.sleep(2)
        self.start_celery_beat()
        time.sleep(2)
        self.start_flower()
        time.sleep(2)
        self.start_django_server()
        time.sleep(2)
        self.start_locust()

        try:
            while True:
                user_input = input(
                    "\nSelect an option:\n"
                    "1. Restart celery worker\n"
                    "2. Restart celery beat\n"
                    "3. Restart flower\n"
                    "4. Restart django server\n"
                    "5. Restart locust\n"
                    "> "
                )

                if user_input == "1":
                    self.stop_celery_worker()
                    self.start_celery_worker()
                elif user_input == "2":
                    self.stop_celery_beat()
                    self.start_celery_beat()
                elif user_input == "3":
                    self.stop_flower()
                    self.start_flower()
                elif user_input == "4":
                    self.stop_django_server()
                    self.start_django_server()
                elif user_input == "5":
                    self.stop_locust()
                    self.start_locust()
                else:
                    print("Invalid option. Please try again.")

        except KeyboardInterrupt:
            self.exit_and_cleanup()

    def run_docker_compose_up(self):
        print("Running docker-compose up...")
        subprocess.run(
            ["docker-compose", "-f", "docker-compose-min.yml", "up", "-d"],
        )
        print("docker-compose up completed.")

    def run_docker_compose_down(self):
        print("Running docker-compose down...")
        subprocess.run(
            ["docker-compose", "-f", "docker-compose-min.yml", "down", "-v"],
        )
        print("docker-compose down completed.")

    def start_django_server(self):
        print("Starting django server...")
        subprocess.Popen(
            ["python", "manage.py", "migrate"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        time.sleep(4)
        self.django_server_process = subprocess.Popen(
            ["python", "manage.py", "runserver"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        print("Django server started.")

    def stop_django_server(self):
        print("Stopping django server...")
        self.django_server_process.terminate()
        print("Django server stopped.")

    def start_locust(self):
        print("Starting locust...")
        self.locust_process = subprocess.Popen(
            ["locust", "-f", "locustfiles/browse_database.py"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        print("Locust started.")

    def stop_locust(self):
        print("Stopping locust...")
        self.locust_process.terminate()
        print("Locust stopped.")

    def start_celery_worker(self):
        print("Starting celery worker...")
        if sys.platform == "win32":
            self.celery_worker_process = subprocess.Popen(
                ["celery", "-A", "config", "worker", "--loglevel=info", "-P", "gevent"],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
            )
        else:
            self.celery_worker_process = subprocess.Popen(
                ["celery", "-A", "config", "worker", "--loglevel=info"],
                creationflags=subprocess.CREATE_NEW_CONSOLE,
            )
        print("Celery worker started.")

    def stop_celery_worker(self):
        print("Stopping celery worker...")
        self.celery_worker_process.terminate()
        print("Celery worker stopped.")

    def start_celery_beat(self):
        print("Starting celery beat...")
        self.celery_beat_process = subprocess.Popen(
            ["celery", "-A", "config", "beat", "--loglevel=info"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        print("Celery beat started.")

    def stop_celery_beat(self):
        print("Stopping celery beat...")
        self.celery_beat_process.terminate()
        print("Celery beat stopped.")

    def start_flower(self):
        print("Starting flower...")
        self.flower_process = subprocess.Popen(
            ["celery", "-A", "config", "flower"],
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        print("Flower started.")

    def stop_flower(self):
        print("Stopping flower...")
        self.flower_process.terminate()
        print("Flower stopped.")

    def exit_and_cleanup(self):
        self.stop_locust()
        time.sleep(1)
        self.stop_django_server()
        time.sleep(1)
        self.stop_flower()
        time.sleep(1)
        self.stop_celery_beat()
        time.sleep(1)
        self.stop_celery_worker()
        time.sleep(1)
        self.run_docker_compose_down()
