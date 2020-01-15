def insertion_sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j =step - 1

        while j >= 0 and key < array[j]:

            # for ascending order, change key<array[j] to key>array[j]

            array[j + 1] = array[j]
            j = j -1
        array[j + 1] = key

data = [6,2,9,7,1,4]
insertion_sort(data)
print('sorted in ascending order: ', data)