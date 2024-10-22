def shell_sort(list1):
    n = len(list1)
    gap = n // 2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if list1[i + gap] > list1[i]:
                    break
                else:
                    list1[i + gap], list1[i] = list1[i], list1[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2


list1 = [7, 23, 1, 89, 27, 25, 99, 46, 37, 23]
print(list1)
shell_sort(list1)
print(list1)