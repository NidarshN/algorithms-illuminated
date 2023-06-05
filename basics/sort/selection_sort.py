import os


def stable_iterative_selection(nums):
    n = len(nums)
    for i in range(n):
        pos = i
        for j in range(i+1, n):
            if (nums[j] < nums[pos] or j < pos):
                pos = j
        key = nums[pos]
        while pos > i:
            nums[pos] = nums[pos - 1]
            pos -= 1
        nums[i] = key
    return nums


def minIndex(a, i, j):
    if i == j:
        return i
    k = minIndex(a, i+1, j)
    return (i if a[i] < a[k] else k)


def recursive_selection(nums, n, index=0):
    if index == n:
        return -1
    k = minIndex(nums, index, n-1)
    if k != index:
        nums[k], nums[index] = nums[index], nums[k]

    recursive_selection(nums, n, index+1)


if __name__ == "__main__":
    # print(stable_iterative_selection([4, 5, 3, 2, 4, 1]))
    arr = [4, 5, 3, 2, 4, 1]
    n = len(arr)
    recursive_selection(arr, n)
    print(arr)
