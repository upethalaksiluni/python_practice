print("---------------------------------------------------------------student name age printing-------------------------------------------------------------------")

def student(name, age):
    print(name, age)
    return 0

student("Silu", 23)
student("Silu", "ggg")

print("---------------------------------------------------------------2 functions printing-------------------------------------------------------------------")

def f1():
    print("True")

    def f2():
        print("False")

    f2()
    return
f1()

print("---------------------------------------------------------------3 numbers analyzing using 2 functions-------------------------------------------------------------------")

def TF(num1, num2, num3):
    if num1 > num2:
        print("true")
    else:
        # Nested function
        def true_func(a, b):
            if a < b:
                print("true")
            else:
                print("false")

        # Call nested function with num2 and num3
        true_func(num2, num3)


# Example usage
TF(5, 10, 15)
TF(10, 5, 3)
TF(5, 10, 5)

print("---------------------------------------------------------------items printing-------------------------------------------------------------------")

def dictFunction(dictionary):
    for i in dictionary.items():
        print(i)
dict = {1: 'A', 2: 'B', 3:'C'}
dictFunction(dict)

print("---------------------------------------------------------------argument printing-------------------------------------------------------------------")


def myFunction(*args):
    for arg in args:
        print(arg)


myFunction("I'm Silu. ", "My", "age", "is", 23)


def myFunction2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


myFunction2(first = "Hello", second = "World")


print("---------------------------------------------------------------BMI Counting-------------------------------------------------------------------")


def bmiCalculator():
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    BMI = weight / (height ** 2)
    print("Your BMI is:", round(BMI))
    return round(BMI)


bmiCalculator()



