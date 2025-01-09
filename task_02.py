import random

def quick_select(arr, k):
    def partition(low, high):
        pivot_index = random.randint(low, high)
        pivot_value = arr[pivot_index]   
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        store_index = low

        for i in range(low, high):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        arr[store_index], arr[high] = arr[high], arr[store_index]
        return store_index

    def quick_select_recursive(low, high, k_smallest):
      
        if low == high:
            return arr[low]
        pivot_index = partition(low, high)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return quick_select_recursive(low, pivot_index - 1, k_smallest)
        else:
            return quick_select_recursive(pivot_index + 1, high, k_smallest)
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах [1, довжина масиву]")

    return quick_select_recursive(0, len(arr) - 1, k - 1)

array = [3, 2, 1, 5, 4]
k = 3
kth_smallest = quick_select(array, k)
print(f"{k}-й найменший елемент: {kth_smallest}")
