from data_generation import generate_dataset
from validators import validate_dataset
import pandas as pd

num_rows = 50000 

dataset = generate_dataset(num_rows)

validate_dataset(dataset)

dataset.to_csv('dataset.csv', index=False)

print(f"Датасет успешно сгенерирован и сохранен. Всего строк: {len(dataset)}")
print(dataset)
