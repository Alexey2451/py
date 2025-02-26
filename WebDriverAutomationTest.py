from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Создаем экземпляр Firefox WebDriver
driver = webdriver.Firefox()

# Открываем сайт Python.org
driver.get("http://www.python.org")

# Проверка, что в заголовке страницы есть слово "Python"
assert "Python" in driver.title

# Находим поле ввода по имени "q" с использованием нового локатора By.NAME и вводим текст для поиска
elem = driver.find_element(By.NAME, "q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

# Убедимся, что поиск вернул результаты
assert "No results found." not in driver.page_source

# Закрываем браузер
driver.close()
