user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))


def division(user_input1, user_input2):

    print(user_input1 / user_input2)


try:
    division(user_input1, user_input2)

except ZeroDivisionError as e:
    print("error occurred", e)


