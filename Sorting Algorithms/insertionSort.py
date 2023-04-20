def insertion_sort1(array):  # this is the preferred version.
    n = len(array)

    for i in range(1, n):
        j = i
        # going leftward to insert element array[i] to proper location in array[0], ..., array[i].
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]  # swap two elements.
            j -= 1


def insertion_sort2(array):
    n = len(array)

    for i in range(1, n):
        j = i
        temp = array[i]
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp


array1 = [1, 5, 2, 7, 3, 4]
array2 = [4, 5, 2, 7, 9, 6]
insertion_sort1(array1)
insertion_sort2(array2)
print("Sorted array1 is: {}".format(array1))
print("Sorted array2 is: {}".format(array2))

array2.pop()
print(array2)