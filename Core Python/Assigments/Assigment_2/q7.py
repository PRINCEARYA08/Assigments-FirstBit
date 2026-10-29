num=123
digit=0
sum=0
while (num>0):
    digit=num%10
    print(digit,end=" ")
    num=num//10
    sum+=digit
print()
print(f'sum of tree digit number is: {sum}')
    