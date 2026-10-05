### 1. calculate factorial
### 2. separate digit
### 3. sum of digit
### 4. reverse the digit



# def fun(n):
#     print('function executing.',n)
#     if(n>1):
#         fun(n-1)
#         print(n)
# n= 5
# fun(n)





def sumofseries(n):
    if(n<=0):
        return 0
    else:
        return n + sumofseries(n-1)
    
n=5
res = sumofseries(n)
print(res)