food_in_kg = float(input()) * 1000
hay_in_kg = float(input()) * 1000
cover_in_kg = float(input()) * 1000
guinea_weight_in_kg = float(input()) * 1000

for day in range(1, 31):
    food_in_kg -= 300
    if day % 2 == 0:
        hay_in_kg -= food_in_kg * 0.05
    if day % 3 == 0:
        cover_in_kg -= guinea_weight_in_kg / 3
    if food_in_kg < 0 and hay_in_kg < 0 and cover_in_kg < 0:
        break

if food_in_kg >= 0 and hay_in_kg >= 0 and cover_in_kg >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kg / 1000:.2f}, Hay: {hay_in_kg / 1000:.2f}, Cover: {cover_in_kg / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")