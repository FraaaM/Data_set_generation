from data_generation import generate_dataset
from validators import validate_dataset
import pandas as pd
from openpyxl import Workbook

print("Введите число запросов, должно быть не менее 50000")

num_rows = int(input())
while num_rows < 50000 and num_rows!=int :
    print("Должно быть не менее 50000!")
    num_rows = int(input())

dataset = generate_dataset(num_rows)

validate_dataset(dataset)

dataset.to_excel('dataset.xlsx', index=False)
#dataset.to_csv('dataset.csv', index=False)


print(f"Датасет успешно сгенерирован и сохранен. Всего строк: {len(dataset)}")
print(dataset)