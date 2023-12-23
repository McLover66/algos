import pandas as pd
from mergesort_utils import merge_sort, merge

# PATH_csv1 = input('введите путь к таблице 1')
# PATH_csv2 = input('введите путь к таблице 2')
# PATH_TO_SAVE = input('введите путь для сохранения')

PATH_csv1 = 'C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи файлы\\random_numbers_for_merge_1.csv'
PATH_csv2 = 'C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи файлы\\random_numbers_for_merge.csv'
PATH_TO_SAVE = 'C:\\Users\\user\\Desktop\\code\\алгоритмы и задачи файлы\\random_numbers_sorted.csv'

df1 = pd.read_csv(PATH_csv1)
df2 = pd.read_csv(PATH_csv2)
column_name = 'Random Numbers'
column_list1 = df1[column_name].astype(int).tolist()
column_list2 = df1[column_name].astype(int).tolist()
column_list = column_list1 + column_list2
sorted_column_list = merge_sort(column_list)
df = pd.DataFrame({'Sorted_column': sorted_column_list})
df.to_csv(PATH_TO_SAVE, index=False)

