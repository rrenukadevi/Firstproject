import tkinter as tk
from tkinter import messagebox

def calculate_health_score(age, bmi, exercise_freq, diet_quality, sleep_quality, stress_level, chronic_condition):
    score = (
        (100 - age * 0.2) * 0.2 +
        (30 - bmi) * 0.2 +
        exercise_freq * 5 +
        diet_quality * 5 +
        sleep_quality * 10 +
        (5 - stress_level) * 5 -
        chronic_condition * 20
    )
    return max(0, min(100, score))  # Ensure score is between 0 and 100

def get_recommendations(score):
    if score >= 80:
        return "You're in great shape! Keep maintaining your healthy lifestyle."
    elif score >= 60:
        return "You're doing well, but there's room for improvement. Consider focusing on better nutrition and regular exercise."
    elif score >= 40:
        return "Your health is okay, but some aspects need attention. Focus on stress management and increasing physical activity."
    else:
        return "Your health needs immediate attention. Please consider consulting a healthcare professional and making significant lifestyle changes."

def calculate():
    try:
        age = int(entry_age.get())
        bmi = float(entry_bmi.get())
        exercise_freq = int(entry_exercise.get())
        diet_quality = int(entry_diet.get())
        sleep_quality = int(entry_sleep.get())
        stress_level = int(entry_stress.get())
        
        # Validate chronic condition input
        chronic_condition_input = entry_condition.get().strip().lower()
        if chronic_condition_input in ['yes', '1']:
            chronic_condition = 1
        elif chronic_condition_input in ['no', '0']:
            chronic_condition = 0
        else:
            messagebox.showerror("Input Error", "Please enter 'Yes' or 'No' for chronic condition.")
            return

        score = calculate_health_score(age, bmi, exercise_freq, diet_quality, sleep_quality, stress_level, chronic_condition)
        recommendation = get_recommendations(score)
        
        result.set(f"Your health score is: {score}")
        messagebox.showinfo("Recommendation", recommendation)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all fields.")

# Create the main window
root = tk.Tk()
root.title("Health & Wellness Bot")

# Create input fields
tk.Label(root, text="Age:").grid(row=0)
tk.Label(root, text="BMI:").grid(row=1)
tk.Label(root, text="Exercise Frequency (per week):").grid(row=2)
tk.Label(root, text="Diet Quality (1-5):").grid(row=3)
tk.Label(root, text="Sleep Quality (hours per night):").grid(row=4)
tk.Label(root, text="Stress Level (1-5):").grid(row=5)
tk.Label(root, text="Chronic Condition (Yes or No):").grid(row=6)

entry_age = tk.Entry(root)
entry_bmi = tk.Entry(root)
entry_exercise = tk.Entry(root)
entry_diet = tk.Entry(root)
entry_sleep = tk.Entry(root)
entry_stress = tk.Entry(root)
entry_condition = tk.Entry(root)

entry_age.grid(row=0, column=1)
entry_bmi.grid(row=1, column=1)
entry_exercise.grid(row=2, column=1)
entry_diet.grid(row=3, column=1)
entry_sleep.grid(row=4, column=1)
entry_stress.grid(row=5, column=1)
entry_condition.grid(row=6, column=1)

# Button to calculate the score
tk.Button(root, text="Calculate Health Score", command=calculate).grid(row=7, column=1)

# Result label
result = tk.StringVar()
tk.Label(root, textvariable=result).grid(row=8, columnspan=2)

# Start the GUI event loop
root.mainloop()
