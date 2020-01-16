taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
taskList=[]
x= type(taskList)
print(x)

# print kes
print(taskList[2][2]['currency'])

# print 560
print(taskList[2][1])

# len of tsk
print(len(taskList[2][2]))


# # change 987 to 789 without using inbuild method
x= str(taskList[3])
y= x[::-1]
a=int(y)
taskList.insert(3,a)


# change the name 'john' to 'jane'
# x= taskList[4][1].replace('John', 'Jane')


print(taskList)
print(y)