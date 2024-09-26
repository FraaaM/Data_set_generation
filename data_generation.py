import random
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict

# Считывание данных из файлов
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Считываем магазины, бренды и категории
#stores = read_data('data/stores.txt')
#brands = read_data('data/brands.txt')
#categories = read_data('data/categories.txt')

banks = ["Сбербанк", "Газпромбанк", "Альфа-Банк", "ВТБ", "Тинькофф", "Райффайзенбанк"]

# Список платёжных систем
payment_systems = ["Visa", "MasterCard", "МИР"]

stores = [
    "М.Видео", "Эльдорадо", "DNS", "Ситилинк", "Технопарк", 
    "Media Markt", "Евросеть", "Техносила", "РЕСТОР", "Технополис"
]

# Список категорий техники
categories = [
    "Смартфоны", "Ноутбуки", "Телевизоры", "Планшеты", "Холодильники", 
    "Стиральные машины", "Кофемашины", "Пылесосы", "Игровые консоли", 
    "Умные часы", "Фотоаппараты", "Колонки", "Наушники"
]

# Список брендов для каждой категории
brands = [
    "Apple", "Samsung", "Lenovo", "LG", "Sony", "Asus", "HP", 
    "Xiaomi", "Huawei", "Acer", "Bosch", "Dyson", "Philips", "JBL"
]

# Генерация случайных координат для магазинов в Санкт-Петербурге
def generate_random_coordinates():
    latitude = round(random.uniform(59.85, 60.0), 8)  # Широта 
    longitude = round(random.uniform(29.80, 30.4), 8)  # Долгота 
    return latitude, longitude

# Генерация случайного времени в пределах текущей даты и времени работы магазина (с 10:00 до 22:00)
def generate_random_time():
    current_date = datetime.now().date()
    start_time = datetime.combine(current_date, datetime.strptime("10:00", "%H:%M").time())
    end_time = datetime.combine(current_date, datetime.strptime("22:00", "%H:%M").time())

    delta = end_time - start_time
    random_seconds = random.randint(0, delta.seconds)
    purchase_time = start_time + timedelta(seconds=random_seconds)

    return purchase_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

# Генерация случайного номера карты и платежной системы
used_cards = defaultdict(int)

def generate_card_number():
    # Генерация случайного номера карты
    card_number = f"{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    
    # Вероятности для банков (например, Сбербанк встречается чаще)
    bank = random.choices(banks, weights=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05], k=1)[0]
    
    # Вероятности для платёжных систем (например, Visa встречается чаще)
    payment_system = random.choices(payment_systems, weights=[0.5, 0.3, 0.2], k=1)[0]
    
    # Увеличиваем счётчик для карты, если она уже была использована
    used_cards[card_number] += 1

    return card_number, bank, payment_system

def generate_unique_card_number():
    while True:
        card_number, bank, payment_system = generate_card_number()
        if used_cards[card_number] <= 5:  # Карта может быть использована до 5 раз
            return card_number, bank, payment_system

# Генерация количества товаров и их стоимости
def generate_quantity_and_price():
    quantity = random.randint(5, 20)
    price = random.randint(1000, 100000)
    return quantity, price

# Генерация одной строки данных о покупке
def generate_purchase_row():
    store = random.choice(stores)  # Выбор случайного магазина
    category = random.choice(categories)  # Выбор случайной категории техники
    brand = random.choice(brands)  # Выбор случайного бренда
    latitude, longitude = generate_random_coordinates()  # Генерация координат
    purchase_time = generate_random_time()  # Генерация случайного времени
    card_number, bank, payment_system = generate_unique_card_number()  # Генерация уникального номера карты
    quantity, price = generate_quantity_and_price()

    return {
        "Магазин": store,
        "Категория": category,
        "Бренд": brand,
        "Дата и время": purchase_time,
        "Широта": latitude,
        "Долгота": longitude,
        "Номер карты": card_number,
        "Банк": bank,
        "Платежная система": payment_system,
        "Количество товаров": quantity,
        "Стоимость": price
    }

# Генерация полного датасета с указанным количеством строк
def generate_dataset(num_rows):
    dataset = []
    for _ in range(num_rows):
        dataset.append(generate_purchase_row())
    return pd.DataFrame(dataset)
