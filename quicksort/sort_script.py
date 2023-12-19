# C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи\\1.0\\random_numbers.csv
# C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи\\1.0\\sort_numbers.csv
from quicksort_handlers import quicksort
import pandas as pd

PATH = input('введите путь к таблице')
df = pd.read_csv(PATH)
left = 0
right = len(df) - 1
column_name = 'Random Numbers'
print(column_name)
quicksort(df, left, right, column_name)

PATH_TO_SAVE = input('куда сохранить')
df.to_csv(PATH_TO_SAVE, index=False)