car = 100
space_in_car = 4.0
drivers = 30
cars_not_driven = car - drivers
cars_driven = drivers

print("There are", car, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("There are", cars_driven, "driven cars today.")
print("The total space in cars is", car * space_in_car)
