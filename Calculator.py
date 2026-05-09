import  math
class Calculator:

    def __init__(self , user_input):
        self.user_input = user_input

    def easy_calculator(self):
        num1 = float(input("Please Enter First Number :"))
        num2 = float(input("Please Enter Second Number :"))
        mode_easy = input("Please Select : + | - | * | / |  ")
        if mode_easy == "+":
            result = num1 + num2
            return f" Result = {result}"
        elif mode_easy == "-":
            result = num1 - num2
            return f" Result = {result}"
        elif mode_easy == "*":
            result = num1 * num2
            return f" Result = {result}"
        elif mode_easy == "/":
            if num1 != 0:
                result = num1 / num2
                return f" Result = {result}"
            else:
                return"Please Enter a Number"
        else:
            return "Error ! 🧨"


    def pro_calculator(self):
        num1 = float(input("Please Enter First Number :"))
        mode_pro = input("Please Select : Logarithm | factorial ")
        if mode_pro.lower() == "Logarithm":
            num2 = float(input("Please Enter Number Of Logarithm :"))
            return f" Result = {math.log(num1, num2)}"
        elif mode_pro.lower() == "Factorial":
            return f"{math.factorial(num1)}"
        else:
            return "Error !!"






calculator = Calculator("")

while True:
    user_input = input("Select Mode : Easy Calculator Or Pro Calculator :  | Or Exit : ")
    if user_input.lower() == "exit":
        print("Goodbye😁")
        break
    if user_input.lower() == "easy calculator":
        easy_calc = calculator.easy_calculator()
        print(easy_calc)
    elif user_input.lower() == "pro calculator":
        pro_calc = calculator.pro_calculator()
        print(pro_calc)


