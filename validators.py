import pandas as pd

# Проверка на повторение номеров карт (не более 5 раз одного номера)
def validate_card_numbers(dataset):
    duplicate_cards = dataset["Номер карты"].value_counts()
    if any(duplicate_cards > 5):
        raise ValueError("Номер карты повторяется более 5 раз.")

# Проверка на наличие пустых или бесплатных товаров
def validate_price(dataset):
    if any(dataset["Стоимость"] <= 0):
        raise ValueError("Стоимость не может быть нулевой или отрицательной.")

# Основная функция проверки
def validate_dataset(dataset):
    validate_card_numbers(dataset)
    validate_price(dataset)
    print("Все проверки успешно пройдены!")
