p = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (R) in percentage: "))
t = float(input("Enter the time (T) in years: "))



amount = p * (1 + r/100)**t

ci = amount - p
print("The compound interest is:", ci)


