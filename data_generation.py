import random
import pandas as pd
from datetime import datetime, timedelta

# Словари для генерации магазинов, категорий и брендов
magazines = [f"Магазин_{i}" for i in range(1, 31)]  # Список магазинов (минимум 30)
categories = [f"Категория_{i}" for i in range(1, 51)]  # Список категорий (минимум 50)
brands = [f"Бренд_{i}" for i in range(1, 501)]  # Список брендов (минимум 500)

# Генерация случайных координат для магазинов в Санкт-Петербурге
def generate_random_coordinates():
    latitude = round(random.uniform(59.85, 60.0), 8)  # Широта 
    longitude = round(random.uniform(29.80, 30.4), 8)  # Долгота 
    return latitude, longitude

# Генерация случайного времени в пределах времени работы магазина (с 10:00 до 22:00)
def generate_random_time():
    current_date = datetime.now().date()
    # Интервал рабочего времени магазина
    start_time = datetime.combine(current_date, datetime.strptime("10:00", "%H:%M").time())
    end_time = datetime.combine(current_date, datetime.strptime("22:00", "%H:%M").time())
    # Генерация случайного времени в пределах рабочего времени
    delta = end_time - start_time
    random_seconds = random.randint(0, delta.seconds)
    purchase_time = start_time + timedelta(seconds=random_seconds)
    # Вывод в формате ISO 8601: '2024-01-22T08:30+03:00'
    return purchase_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')


# Генерация случайного номера карты и платежной системы
def generate_card_number():
    bank_codes = ['1234', '5678', '4321', '8765']  # Пример банков
    return f"{random.choice(bank_codes)} {random.choice(bank_codes)} {random.choice(bank_codes)} {random.choice(bank_codes)}"

# Генерация количества товаров и их стоимости
def generate_quantity_and_price():
    quantity = random.randint(5, 20)  # Количество товаров (минимум 5)
    price = random.randint(1000, 100000)  # Стоимость от 1 000 до 100 000 руб
    return quantity, price

# Генерация одной строки данных о покупке
def generate_purchase_row():
    store = random.choice(magazines)
    category = random.choice(categories)
    brand = random.choice(brands)
    latitude, longitude = generate_random_coordinates()
    purchase_time = generate_random_time()
    card_number = generate_card_number()
    quantity, price = generate_quantity_and_price()

    return {
        "Магазин": store,
        "Категория": category,
        "Бренд": brand,
        "Дата и время": purchase_time,
        "Широта": latitude,
        "Долгота": longitude,
        "Номер карты": card_number,
        "Количество товаров": quantity,
        "Стоимость": price
    }

def generate_dataset(num_rows):
    dataset = []
    for _ in range(num_rows):
        dataset.append(generate_purchase_row())
    return pd.DataFrame(dataset)
