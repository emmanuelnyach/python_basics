my_num =[1,2,3,4,5, 6,7]
my_float =[10.1, 10.2, 10.3, 10.4]
my_pets = ['dog', 'cat', 'hen', 'rabbit']
my_bools = [True, False, True, False]
mix = [1, 'hello', True, 10.5]
list_of_lists = [[1,2,3,4], [10, '22', True, [9,9,False]],[10.5]]


# list indexing
print("get num", my_num[3])

# list slicing
print(my_num[1:5])

# reverse
print(my_num[::-1])
print("".join(reversed(my_pets)))


x = 'abcde'
# print(x[::-])

print(list_of_lists[1][3][2])

age = 18
print('my age is {}'.format(age))





tol = (10.5, ['we',True, False], 10)
y= tol[1].append('1')
print(y)