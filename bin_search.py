def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        # Если среднее пусто сдвигаем налево или направо
        if left<mid<right:
            mid = mid if arr[mid] else mid-1 if not not arr[mid-1] else mid+1
        # Если остались только пустые значения завершаем цикл 
        if not arr[left] and not arr[mid] and not arr[right]:
            break
        # Проверка среднего элемента
        if arr[mid] == x:
            return mid
        # Если x больше, игнорируем левую половину
        elif arr[mid] < x:
            left = mid + 1
        # Если x меньше, игнорируем правую половину
        else:
            right = mid - 1

    # Элемент не найден
    return -1


# Пример использования
arr = [1, 2, None, None, 5, 6, 7, None, 10, 11]
x = 10

result = binary_search(arr, x)
if result != -1:
    print(f"Result: {result}")
else:
    print("Element not found in array")