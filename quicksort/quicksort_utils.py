def partition(data, low, high, column_name):
    E = low
    G = low
    i = low
    while i <= high:
        el_i = data.at[i, column_name]
        if el_i < data.at[E, column_name]:
            data.at[i, column_name] = data.at[G, column_name]
            data.at[G, column_name] = data.at[E, column_name]
            data.at[E, column_name] = el_i
            E += 1
            G += 1
            i += 1
        elif el_i == data.at[E, column_name]:
            data.at[i, column_name] = data.at[G, column_name]
            data.at[G, column_name] = data.at[E, column_name]
            G += 1
            i += 1
        elif el_i > data.at[E, column_name]:
            i += 1
    return E

def quicksort(data, left, right, column_name):
    if left < right:
        pivot = partition(data, left, right, column_name)
        quicksort(data, left, pivot - 1, column_name)
        quicksort(data, pivot + 1, right, column_name)

