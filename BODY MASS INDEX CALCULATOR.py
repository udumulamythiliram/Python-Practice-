#BODY MASS INDEX CALCULATOR

name = input("whats is your name:")
height = float(input("what is your height in meters;"))
weight = float(input("what is your weight in kg:"))
bmi = weight / height **2

print(f"Health report for {name}:")
print(f"BMI:{bmi}")

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"


match category:
    case "Underweight":
        print("You are underweight and may need to gain weight for optimal health.")
    case "Normal weight":
        print("You have a normal weight. Keep up the good work!")
    case "Overweight":
        print("You are overweight and may benefit from weight loss for better health.")
    case "Obese":
        print("You are obese and should consider consulting a healthcare professional for weight management.")
   