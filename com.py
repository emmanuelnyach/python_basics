marks = float(input('enter your name: '))

if marks>=80 and marks<=100:
    print("Grade A")

elif marks >= 70 and marks<80:
    print('Grade B')

elif marks >= 60 and marks<70:
    print('Grade c')

elif marks >= 40 and marks<60:
    print('Grade D')
elif marks > 0 and marks <40 :
    print('fail!!')

else:
    print('invalid marks!!')