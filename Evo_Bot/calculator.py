import  math
class Calculator:

    def __init__(self , user_input):
        self.user_input = user_input

    def easy_calculator(self):
        num1 = float(input("لطفا عدد اول رو وارد کن :"))
        num2 = float(input("لطفا عدد دوم رو وارد کن :"))
        mode_easy = input("عملگر رو انتخاب کن : + | - | * | / :")
        if mode_easy == "+":
            result = num1 + num2
            return f" حاصل = {result}"
        elif mode_easy == "-":
            result = num1 - num2
            return f"حاصل = {result} "
        elif mode_easy == "*":
            result = num1 * num2
            return f" حاصل =  {result}"
        elif mode_easy == "/":
            if num1 != 0:
                result = num1 / num2
                return f" حاصل =  {result}"
            else:
                return"لطفا عدد وارد کن"
        else:
            return " خطا ! 🧨"


    def pro_calculator(self):
        num1 = float(input("لطفا عدد رو وارد کن :"))
        mode_pro = input("عملگر رو انتخاب کن : لوگاریتم | فاکتوریل ")
        if mode_pro.lower() == "لوگاریتم":
            num2 = float(input("لطفا عدد برای تبدیل به لوگاریتم رو بنویس :"))
            return f" Result = {math.log(num1, num2)}"
        elif mode_pro.lower() == "فاکتوریل":
            return f"{math.factorial(num1)}"
        else:
            return "خطا !!"






calculator = Calculator("")



