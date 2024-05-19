import unittest
from app import app, convert


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_input_value_is_numeric(self):
        # Проверяем, что вводимое значение является числом
        input_value = '100'  # Пример вводимого значения
        self.assertTrue(input_value.replace('.', '', 1).isdigit())

    def test_decimal_input_value(self):
        # Проверяем десятичное значение
        input_value = '3.14'
        self.assertTrue(input_value.replace('.', '', 1).isdigit())

    def test_invalid_input_value(self):
        # Проверяем недопустимое значение (например, буквы)
        input_value = 'abc'
        self.assertFalse(input_value.replace('.', '', 1).isdigit())


if __name__ == '__main__':
    unittest.main()
