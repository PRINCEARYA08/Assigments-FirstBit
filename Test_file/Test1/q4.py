#area = float(input("Enter area of the house: "))
#interior = int(input("Enter interior cost : "))
#exterior = int(input("Enter exterior cost: "))



area = 100
interior = 20
exterior = 15

# 2*4=8
#8-2   (area of same wall) = 6
total_area = area * 6

interior_cost = total_area * interior
exterior_cost = total_area * exterior

print("Interior Cost =", interior_cost)
print("Exterior Cost =", exterior_cost)
print("Total Cost =", interior_cost + exterior_cost)