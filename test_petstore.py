import requests

BASE_URL = "https://petstore.swagger.io/v2"


# ============================
# Тесты для сущности PET
# ============================

def test_create_pet():
    """Создание нового питомца"""
    payload = {
        "id": 1,
        "name": "Doggie",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Doggie"


def test_get_pet_by_id():
    """Получение питомца по ID"""
    # Создаём питомца перед тестом
    test_create_pet()

    pet_id = 1
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id


def test_update_pet_status():
    """Обновление статуса питомца"""
    # Создаём питомца перед тестом
    test_create_pet()

    pet_id = 1
    payload = {
        "id": pet_id,
        "name": "Doggie",
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"


def test_delete_pet():
    """Удаление питомца"""
    # Создаём питомца перед тестом
    test_create_pet()

    pet_id = 1
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 200


def test_get_nonexistent_pet():
    """Попытка запроса несуществующего питомца"""
    pet_id = 9999
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    assert response.status_code == 404


# ============================
# Тесты для сущности USER
# ============================

def test_create_user():
    """Создание нового пользователя"""
    payload = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200


def test_get_user_by_username():
    """Получение пользователя по имени"""
    # Сначала создаём пользователя
    test_create_user()

    username = "testuser"
    response = requests.get(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200
    assert response.json()["username"] == username


def test_user_login():
    """Логин пользователя"""
    # Сначала создаём пользователя
    test_create_user()

    params = {
        "username": "testuser",
        "password": "password123"
    }
    response = requests.get(f"{BASE_URL}/user/login", params=params)
    assert response.status_code == 200


def test_user_logout():
    """Логаут пользователя"""
    response = requests.get(f"{BASE_URL}/user/logout")
    assert response.status_code == 200


def test_delete_user():
    """Удаление пользователя"""
    # Прямое создание пользователя
    payload = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890"
    }
    response = requests.post(f"{BASE_URL}/user", json=payload)
    assert response.status_code == 200, f"User creation failed: {response.text}"

    # Удаление пользователя
    username = "testuser"
    response = requests.delete(f"{BASE_URL}/user/{username}")
    assert response.status_code == 200, f"User deletion failed: {response.text}"



# ============================
# Тесты для сущности STORE
# ============================

def test_get_inventory():
    """Получение информации об инвентаре магазина"""
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert "available" in response.json()


def test_place_order():
    """Размещение нового заказа"""
    payload = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2023-11-01T12:00:00Z",
        "status": "placed",
        "complete": True
    }
    response = requests.post(f"{BASE_URL}/store/order", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"


def test_get_order_by_id():
    """Получение заказа по ID"""
    # Сначала размещаем заказ
    test_place_order()

    order_id = 1
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id


def test_delete_order():
    """Удаление заказа по ID"""
    # Сначала создаём заказ
    test_place_order()

    order_id = 1
    response = requests.delete(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 200


def test_get_nonexistent_order():
    """Попытка запроса несуществующего заказа"""
    order_id = 9999
    response = requests.get(f"{BASE_URL}/store/order/{order_id}")
    assert response.status_code == 404
