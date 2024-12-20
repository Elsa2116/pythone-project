weight = float(input("enter your weight in kilogram: "))
height = float(input("enter your height in meter: "))
bmi = (weight/(height*height))
bmi = round(bmi, 2)
print(f"Your bmi is = {bmi}" )

