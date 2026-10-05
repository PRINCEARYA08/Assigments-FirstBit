length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
radius = float(input("Enter radius: "))

rectangle_area = length * breadth
semicircle_area = (3.14 * radius * radius)/2


total_area = rectangle_area + semicircle_area

print("Area =", total_area)