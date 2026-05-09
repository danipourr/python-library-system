import random
import  json
import os


from Calculator import calculator


class ChatBot:
    def __init__(self):
        self.file_name = "Evo_Bot.json"
        if os.path.exists(self.file_name):
            self.load_data()

        self.dictionary_chat = {
            "سلام" : ["سلام , چطور میتونم کمکت کنم ؟" , "سلام رفیق 🙌 ، چطور میتونم کمکت کنم؟"] ,
            "من خوبم" : ["خوشحالم که حالت خوبه رفیق 😊 ، چه خبر ؟" ],
            "حالت چطوره" : ["من خوبم 😁 ، تو چطوری ؟"],
            "اسمت چیه" : ["اسم من اوو بات هست 😁اسم تو چیه ؟"],
            "خودتو معرفی کن" : ["حتما 😊  من یه مدل چت بات هستم که برای صحبت کردن و راه حل دادن برای مسیًله های شما ساخته شدم 😁"],
            "حالم خوب نیست" : ["اوه رفیق 😢، چرا حالت بده ؟"]

        }
        self.joke = {
            "میدونی چرا سر نمکدون سوراخ داره ؟" : "برا اینکه نمک ها خفه نشن😂",
            "میدونی چرا ماهی ها دست نمیدن ؟" : " برا اینکه دستاشون خیسه 😂",
            "میدونی وقتی یه فلش تعجب کنه چی میگه ؟" : "میگه وای حجمااام😂",
            "میدونی اگه حیوانات نادرو شکار کنیم چی میشه ؟" : "نادر نارحت میشه😂" ,

        }

    def response(self , user):
        if user in self.dictionary_chat:
            return random.choice(self.dictionary_chat[user])
        elif user not in self.dictionary_chat:
            ch_learn = input("من اینو بلد نیستم میخوای بهم یاد بدی؟ آره یا نه؟")
            if ch_learn == "اره":
                print("باشه ، پس بهم کلید و مقدار رو بده")
                key_user = input("کلید رو بهم بده :")
                value_user = input("مقدار رو بهم بده :")
                self.dictionary_chat[key_user] = [value_user]
                self.save_data()
                return "اوکی یاد گرفتم 😁"
            elif (ch_learn == "نه"):
                return "اوکی 😢"
            else:
                return "لطفا درست انتخاب کن !"

    def name(self , user):
        if user.lower() == "اوو بات":
            help_chat_bot = input("چطور میتونم کمکت کنم ؟")
            return "اوکی 😊"


    def joke_user(self , user):
        if user == "برام جوک بگو" :
            random_joke = random.choice(list(self.joke.items()))
            return random_joke

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            json.dump(self.dictionary_chat, f, ensure_ascii=False, indent=4)

    def load_data(self):
        with open(self.file_name, "r", encoding="utf-8") as f:
            self.dictionary_chat = json.load(f)

    def calculator(self , user):
        while True:
            user_input = input("لطفا انتخاب کن : ماشین حساب ساده | ماشین حساب پرو | خروج :")
            if user_input.lower() == "خروج":
                print("خدانگهدار😁")
                break
            if user_input.lower() == "ماشین حساب ساده":
                easy_calc = calculator.easy_calculator()
                print(easy_calc)
            elif user_input.lower() == "ماشین حساب پرو":
                pro_calc = calculator.pro_calculator()
                print(pro_calc)

chat_bot = ChatBot()
while True:
    user = input("شما در حال چت با چت بات هستید :")

    if user == "خروج":
        print("خدانکهدار 😊")
        break

    joke = chat_bot.joke_user(user)
    if joke:
        print("چت بات :", joke)
        continue

    response_ch = chat_bot.response(user)
    if response_ch:
        print("چت بات : ", response_ch)

    name_ch = chat_bot.name(user)
    if name_ch:
        print("چت بات :", name_ch)

    calculator_ch = chat_bot.calculator(user)
    if calculator_ch:
        print("چت بات : ", calculator_ch)