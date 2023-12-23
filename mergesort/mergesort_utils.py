def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = (len(list) // 2)
    left = list[:mid]
    right = list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    i = g = 0
    while i < len(left) and g < len(right):
        if left[i] <= right[g]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[g])
            g += 1
    result.extend(left[i:])
    result.extend(right[g:])
    return result