numbers = [1023, 43566, 678345, 54767]
# print(max(numbers))

print(numbers[0::3])

num = (1,2,3,4,5,6,7,8,9,10)

new =[]

new.append(num[0])
new.append(num[-1])

print(new)

first_num =  num[0:5]
second_num= num[5:]

f = str(first_num)
p = str(second_num)

h = str(num)
print(type(h))
print(f.strip('()'))


s= 'xyx'
s= s.replace('x', 'yy')
print(s)
print(len(s))