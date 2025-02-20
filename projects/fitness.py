# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    workouts.append(f"{workout_type} - {duration}")
    print(f"✅ Logged {duration}-minute {workout_type} workout.")


def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    calories.append(calories_consumed)
    print(f"🍗 Added a calorie intake of {calories_consumed} calories.")


def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_workout = 0
    for i in range(len(workouts)):
        workout = str(workouts[i])
        details = workout.split(' - ')
        total_workout += int(details[1])

    total_calories = sum(calories)

    print(f"Total workout time: {total_workout} minutes.")
    print(f"Total calories consumed: {total_calories} calories.")

    encouragement_system()
    print("Keep going, consistency is key 🔑!")


def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    global workouts
    global calories

    workouts = []
    calories = []

    print("Cleared all history data.")


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    global workout_goal
    global calorie_goal

    workout_goal = int(workout_minutes)
    calorie_goal = int(calorie_limit)

    print(f"Set a workout goal of {workout_minutes} minutes and a calorie goal of {calorie_limit} calories")


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    total_workout = 0
    for i in range(len(workouts)):
        workout = str(workouts[i])
        details = workout.split(' - ')
        total_workout += int(details[1])

    total_calories = sum(calories)

    print(f"Total workout time today: {total_workout} minutes. \n"
          f"Goal: {workout_goal} minutes.\n")
    print(f"Total calorie intake today: {total_calories} calories. \n"
          f"Goal: {calorie_goal} calories.\n")

    if total_workout > workout_goal and total_calories > calorie_goal:
        print("Congratulations! You completed all of your goals for today.")
    else:
        print(f"Keep going, you're one step away from completing your goals!")


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            workout_type = input("Enter workout type: ")
            duration = int(input("Enter workout duration (in minutes): "))
            log_workout(workout_type, duration)
        elif choice == '2':
            calorie_intake = int(input("Enter calorie intake: "))
            log_calorie_intake(calorie_intake)
        elif choice == '3':
            view_progress()
        elif choice == '4':
            reset_progress()
        elif choice == '5':
            workout_minutes = input("Enter workout goal (in minutes): ")
            calorie_limit = int(input("Enter daily calorie intake goal: "))
            set_daily_goals(workout_minutes, calorie_limit)
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
