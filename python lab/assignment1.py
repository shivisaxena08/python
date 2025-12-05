
print("Welcome to the Daily Calorie Tracker CLI!")
print("This tool helps you log your meals and track your calorie intake.\n")

meals = []
calories = []

num_meals = int(input("How many meals did you have today? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    meal_calories = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(meal_calories)

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))
if total_calories > daily_limit:
    status_message = "⚠️ Warning: You have exceeded your daily calorie limit!"
else:
    status_message = "✅ Great job! You are within your daily calorie limit."

print("\n----- Daily Calorie Summary -----")
print(f"{'Meal Name':<15}{'Calories'}")
print("-" * 30)
for i in range(len(meals)):
    print(f"{meals[i]:<15}{calories[i]}")
print("-" * 30)
print(f"{'Total':<15}{total_calories}")
print(f"{'Average':<15}{average_calories:.2f}")
print(status_message)

save = input("\nDo you want to save this session to a file? (yes/no): ").lower()

if save == "yes":
    from datetime import datetime
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Log\n")
        file.write(f"Date: {datetime.now()}\n\n")
        file.write(f"{'Meal Name':<15}{'Calories'}\n")
        file.write("-" * 30 + "\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}{calories[i]}\n")
        file.write("-" * 30 + "\n")
        file.write(f"{'Total':<15}{total_calories}\n")
        file.write(f"{'Average':<15}{average_calories:.2f}\n")
        file.write(status_message + "\n")

    print(f"\nSession saved successfully in '{filename}'.")
else:
    print("\nSession not saved.")
