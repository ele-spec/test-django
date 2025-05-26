# blog/tests/test_services.py

from django.test import TestCase
from blog.services import example_service_function # Переконайтеся, що тут латинська 'c'

class ServicesTest(TestCase):
    def test_example_service_function(self):
        """Перевіряє, чи сервісна функція працює коректно"""
        result = example_service_function("Test input")
        # ОНОВІТЬ ЦЕ: Expected output має відповідати логіці функції
        # Якщо функція повертає "Processed: Test input", то так і має бути:
        self.assertEqual(result, "Processed: Test input")