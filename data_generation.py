import random
import pandas as pd
from datetime import datetime, timedelta
from collections import defaultdict
from data import *

def generate_random_time(open_t, close_t):
    current_date = datetime.now().date()
    open_time = datetime.combine(current_date, datetime.strptime(open_t, "%H:%M").time())
    close_time = datetime.combine(current_date, datetime.strptime(close_t, "%H:%M").time())

    delta = close_time - open_time
    random_seconds = random.randint(0, delta.seconds)
    purchase_time = open_time + timedelta(seconds=random_seconds)

    return purchase_time.strftime('%Y-%m-%dT%H:%M:%S+03:00')

used_cards = defaultdict(int)
def generate_card_number():
    bank = random.choices(banks, weights=[sber, tenek, alf, vtb, psb], k=1)[0]
    bin_code = random.choice(bin_codes[bank])
    payment_system = random.choices(payment_systems, weights=[mir, visa, master], k=1)[0] 
    payment_system_code = payment_systems_codes[payment_system]
    card_number = ''.join(random.choices('0123456789', k=10))
    
    used_cards[card_number] += 1
    return f"{payment_system_code}{bin_code}{card_number}", bank, payment_system

def generate_unique_card_number():
    while True:
        card_number, bank, payment_system = generate_card_number()
        if used_cards[card_number] <= 5:  # Карта может быть использована до 5 раз
            return card_number, bank, payment_system


def generate_quantity_and_price(a):
    quantity = random.randint(5,10)
    price = (random.randint( a[len(a)-2] , a[len(a)-1] )) * quantity
    return quantity, price


print("Напишите вероятность для каждого банка , в сумме должно быть 1!")
print("1 - Сбербанк, 2 - Тинькофф, 3 - Альфа-Банк , 4 - ВТБ, 5 - ПСБ")
sber = float(input())
tenek = float(input())
alf = float(input())
vtb = float(input())
psb = float(input())   
print("Введите вероятность для платёжных систем: 1 - МИР, 2 - Visa, 3 - MasterCard")
mir = float(input())
visa = float(input())
master = float(input())



def generate_purchase_row():

    store = random.choice(stores)
    latitude, longitude, open_t, close_t = random.choice(stores_data[store]) 
    purchase_time = generate_random_time(open_t,close_t)
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
