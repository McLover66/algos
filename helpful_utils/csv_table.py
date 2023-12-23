import pandas as pd
import random
random_numbers = [random.randint(1, 1000) for _ in range(100)]
df = pd.DataFrame({'Random Numbers': random_numbers})
print(df.head(10))
df.to_csv('C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи файлы\\random_numbers_for_merge_1.csv', index=False)
