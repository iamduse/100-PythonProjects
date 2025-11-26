print('''  
WELCOME TO BMI CALCULATOR PROGRAM
''')
weight = float(input("Enter your weight? "))
height = float(input("Enter your Height? "))

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    print(bmi)
    print('underweight')
elif bmi >= 18.5 :
    print(bmi)
    print("normal weight")
elif bmi == 25 or bmi > 25:
    print(bmi)
    print("overweight")
else:
    print('not found')