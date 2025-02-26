import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Импортируем новый модуль для локаторов


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        """Инициализация WebDriver перед каждым тестом"""
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        """Тест поиска 'pycon' на сайте python.org"""
        driver = self.driver
        driver.get("http://www.python.org")
        # Проверяем, что заголовок страницы содержит "Python"
        self.assertIn("Python", driver.title)
        # Находим поле поиска и отправляем запрос
        elem = driver.find_element(By.NAME, "q")  # Обновленный метод
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        # Проверяем, что результаты есть
        assert "No results found." not in driver.page_source

    def tearDown(self):
        """Закрытие браузера после выполнения теста"""
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
