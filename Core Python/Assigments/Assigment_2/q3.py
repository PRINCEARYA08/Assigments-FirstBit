# feet = float(input("Enter the feet: "))
# inches = float(input("Enter the inches: "))


# total_inches=(feet*12)+inches



# total_centimeters = total_inches *2.54

# meters = total_centimeters // 100

# # print(total_inches)
# # print(total_centimeters)
# # print(meters)

# remaining_centimeters = total_centimeters % 100

# print("feet",feet)
# print("inches",total_inches)
# print("meters",meters)
# print("centimeters", remaining_centimeters)


feet = float(input("Enter the feet: "))
inches = float(input("Enter the inches: "))

total_inches = (feet * 12) + inches

total_centimeters = total_inches * 2.54

meters = total_centimeters // 100
remaining_centimeters = total_centimeters % 100

print("Feet =", feet)
print("Total inches =", total_inches)
print("Meters =", meters)
print("Centimeters =", remaining_centimeters)