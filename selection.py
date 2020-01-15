def selection_sort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step+1, size):
            # to sort in descending order, change > to < in this line
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-7, 2, -24,9,6,-36]
size = len(data)
selection_sort(data, size)
print('data in ascending order: ', data)