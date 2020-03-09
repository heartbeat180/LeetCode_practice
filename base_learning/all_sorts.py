# coding: utf-8

# 各排序算法都可以加入排序方向参数，用来确定升序或降序
# 加入order传参， **_sort(alist,order)
# 加条件判断即可 if (alist[j] > alist[j+1] and order>0) or (alist[j] < alist[j+1] and order <0):

## 冒泡排序
def bubble_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        count = 0
        for j in range(n - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                count += 1
        if count == 0:  ## 优化最小复杂度，如果i没产生交换，下次即可跳过
            break
    return alist


## 选择排序
def selection_sort(alist):
    n = len(alist)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            # if alist[j] < alist[min_idx]:
            #     alist[min_idx],alist[j] = alist[j], alist[min_idx]
            if alist[j] < alist[min_idx]:
                min_idx = j
        alist[i], alist[min_idx] = alist[min_idx], alist[i]
    return alist


## 插入排序
def insert_sort(alist):
    n = len(alist)
    for i in range(1, n):
        key = alist[i]
        j = i - 1
        while j >= 0 and key < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key


## 希尔排序
def shell_sort(alist):
    n = len(alist)
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n):
            key = alist[i]
            j = i
            while j >= gap and key < alist[j - gap]:
                alist[j] = alist[j - gap]
                j -= gap
            alist[j] = key
        gap = int(gap / 2)
        # return alist


## 快速排序
def quick_sort(alist):
    if len(alist) <= 1:
        return alist
    pivot = alist[len(alist) // 2]  # 选一个基准值
    #  分割
    left = [x for x in alist if x < pivot]
    middle = [x for x in alist if x == pivot]
    right = [x for x in alist if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)  # 递归排序子序列

## 归并排序
def mergeSort(alist):
    if len(alist) < 2:
        return alist
    middle  = len(alist)//2
    left, right = alist[0:middle], alist[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result=[]
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

# 计数排序
def countSort(alist):
    max_num = max(alist)
    sorted_i = 0
    blist = [0]*(max_num + 1)
    for i in range(len(alist)):
        if not alist[i]:
            blist[alist[i]] = 0
        blist[alist[i]] += 1
    for j in range(max_num +1):
        while blist[j]>0:
            alist[sorted_i] = j
            sorted_i += 1
            blist[j] -= 1
    return alist



if __name__ == "__main__":
    import numpy as np

    a = np.arange(10)
    np.random.shuffle(a)
    print(bubble_sort(a))

    a = np.arange(5)
    np.random.shuffle(a)
    print(selection_sort(a))

    a = np.arange(6)
    np.random.shuffle(a)
    insert_sort(a)
    print(a)

    a = np.arange(7)
    np.random.shuffle(a)
    shell_sort(a)
    print(a)

    a = np.arange(8)
    np.random.shuffle(a)
    print(quick_sort(a))

    a = np.arange(9)
    np.random.shuffle(a)
    print(quick_sort(a))

    a = np.arange(10)
    np.random.shuffle(a)
    print(quick_sort(a))