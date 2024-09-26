from data_generation import generate_dataset
from validators import validate_dataset
import pandas as pd

# Параметры генерации

num_rows = 200  # Количество строк в датасете

# Генерация датасета
dataset = generate_dataset(num_rows)

# Проверка датасета на соответствие ограничениям
validate_dataset(dataset)

# Сохранение датасета в файл
dataset.to_csv('dataset.csv', index=False)

print(f"Датасет успешно сгенерирован и сохранен. Всего строк: {len(dataset)}")
print(dataset)
