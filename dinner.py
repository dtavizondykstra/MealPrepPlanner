from random import randint

print("==================================================")
print("\nWelcome to the Python 3 Meal Prepper!")
print("\nThis week we'll have:")

#Soup Option
soup = randint (0,3)
if soup == 0:
    soup = "Lentil Soup"
elif soup == 1:
    soup = "Southwest Chicken Soup"
elif soup == 2:
    soup = "Minestrone"
elif soup == 3:
    soup = "Chili"
print(f"Soup: {soup}")

#Meat Option
meat = randint (4,8)
if meat == 4:
    meat = "Ground Chicken/Turkey Southwest Bowls"
elif meat == 5:
    meat = "Veggie Omelets"
elif meat == 6:
    meat = "Turkey Breast and Vegetables"
elif meat == 7:
    meat = "Italian Turkey and Spaghetti Squash"
elif meat == 8:
    meat = "Chicken Breast and Vegetables"
print(f"Meat: {meat}")

#fish Option
fish = randint (0,2)
if fish == 0:
    fish = "Salmon and Vegetables"
elif fish == 1:
    fish = "Tuna Steak and Vegetables"
elif fish == 2:
    fish = "Cod and Vegetables"
print(f"Fish: {fish}")

#Salad Option
salad = randint (0,2)
if salad == 0:
    salad = "Cobb Salad"
elif salad == 1:
    salad = "Kale Salad"
elif salad == 2:
    salad = "Greek Salad"
print(f"Salad: {salad}\n")
print("==================================================")
print("\n" * 2)
