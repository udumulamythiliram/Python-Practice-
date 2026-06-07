
def get_bmi( weight, height):
    return weight / height**2


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input())
    height = float(input())
    bmi = get_bmi(weight, height)
    print(bmi)
    print(get_category(bmi))

if __name__ == "__main__":
    main()
