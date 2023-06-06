def sort_insertion(arr, n):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    n = len(arr)
    sort_insertion(arr, n)
    print(arr)