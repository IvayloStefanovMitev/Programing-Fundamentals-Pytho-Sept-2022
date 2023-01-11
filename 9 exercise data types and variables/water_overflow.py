lines = int(input())
tank_capacity = 255
liters_in = 0
for line in range(1, lines + 1):
    liters_of_water = int(input())

    if tank_capacity - liters_of_water < 0:
        tank_capacity += liters_of_water
        print("Insufficient capacity!")
        continue
    tank_capacity -= liters_of_water
    liters_in += liters_of_water
print(liters_in)
