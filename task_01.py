def find_min_max(arr):
    def divide_and_conquer(start, end):
        if start == end:
            return arr[start], arr[start]

        if end == start + 1:
            return (min(arr[start], arr[end]), max(arr[start], arr[end]))

        mid = (start + end) // 2
        left_min, left_max = divide_and_conquer(start, mid)
        right_min, right_max = divide_and_conquer(mid + 1, end)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        return None, None

    return divide_and_conquer(0, len(arr) - 1)

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_min_max(array)
print(f"Мінімум: {min_value}, Максимум: {max_value}")
