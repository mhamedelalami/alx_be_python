# daily_reminder.py

# Prompt for a Single Task
Task = input("Enter your task:  ")
Priority = input("Enter the priority level (high, medium, low): ").lower()
TimeBound = input("Is it time-bound? (yes or no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match Priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority."

# Check if task is time-bound
if time_bound == "yes":
    reminder += " It requires immediate attention today!"

# Display the customized reminder
print(reminder)
