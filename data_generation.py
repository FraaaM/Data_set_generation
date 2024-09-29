import random
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
from data import *

def generate_random_time(start_t, end_t):
    current_date = datetime.now().date()
    start_time = datetime.combine(current_date, datetime.strptime(start_t, "%H:%M").time())
    end_time = datetime.combine(current_date, datetime.strptime(end_t, "%H:%M").time())

    delta = end_time - start_time
    random_seconds = random.randint(0, delta.seconds)
    purchase_time = start_time + timedelta(seconds=random_seconds)

    return purchase_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')


used_cards = defaultdict(int)
def generate_card_number():

    card_number = f"{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}"
    bank = random.choices(banks, weights=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05], k=1)[0]
    payment_system = random.choices(payment_systems, weights=[0.5, 0.3, 0.2], k=1)[0]
    used_cards[card_number] += 1

    return card_number, bank, payment_system

def generate_unique_card_number():
    while True:
        card_number, bank, payment_system = generate_card_number()
        if used_cards[card_number] <= 5:  # Карта может быть использована до 5 раз
            return card_number, bank, payment_system


def generate_quantity_and_price(a):
    quantity = random.randint(1, 10)
    price = random.randint( a[len(a)-2] , a[len(a)-1] ) 
    return quantity, price


def generate_purchase_row():

    store = random.choice(stores)
    latitude, longitude, start_t, end_t = random.choice(stores_data[store]) 
    purchase_time = generate_random_time(start_t,end_t)
    category = random.choice(categories[store])  
    brand = random.choice(brands[category][ : (len(brands[category]) - 2)])  
    card_number, bank, payment_system = generate_unique_card_number()   
    quantity, price = generate_quantity_and_price(brands[category])
    
    return {
        "Магазин": store,
        "Широта": latitude,
        "Долгота": longitude,
        "Дата и время": purchase_time,
        "Категория": category,
        "Бренд": brand,
        "Номер карты": card_number,
        "Банк": bank,
        "Платежная система": payment_system,
        "Количество товаров": quantity,
        "Стоимость": price
    }

def generate_dataset(num_rows):
    dataset = []
    for _ in range(num_rows):
        dataset.append(generate_purchase_row())
    return pd.DataFrame(dataset)
