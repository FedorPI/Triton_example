import time
from locust import HttpUser, task, between
import requests

# Путь к файлу изображения
IMAGE_PATH = "test_images/1.jpg"
# URL вашего API
API_URL = "/predict/"
# Имя модели для использования
MODEL_NAME = "classifier_trt"

class ApiUser(HttpUser):
    wait_time = between(0, 0)  # Время ожидания между задачами (в секундах)

    @task
    def predict(self):
        try:
            with open(IMAGE_PATH, "rb") as image_file:
                files = {
                    "file": ("1.jpg", image_file, "image/jpeg")  # Файл изображения
                }
                params = {
                    "model_name": MODEL_NAME  # Параметр model_name
                }
                # Отправляем POST-запрос
                self.client.post(API_URL, params=params, files=files)
        except Exception as e:
            print(f"Error during request: {e}")