class Phone_Book:
    def __init__(self):
        self.dic_phone_book = {}

    def add_contact(self):
        name_contact = input("Please Write The Name :")
        phone_contact = input("Please Write The Phone Number :")
        self.dic_phone_book[name_contact] = phone_contact
        return "Ok , Contact Added Successfully"

    def search_contact(self):
        search_cont = input("Please Select Search : Name | Phone Number :")
        if search_cont.lower() == "name":
            name_con_search = input("Please Write The Name :")
            if name_con_search in self.dic_phone_book:
                return f"Name {name_con_search} Has Been Found"
            else:
                return f"Name {name_con_search} Has Not Been Found"

        elif search_cont.lower() == "phone number" or "phone":
            phone_con_search = input("Please Write The Phone Number :")
            if phone_con_search in self.dic_phone_book:
                return f"Name {phone_con_search} Has Been Found"
            else:
                return f"Name {phone_con_search} Has Not Been Found"


    def delete_contact(self):
        name_del_con = input("Please Write The Name For Delete :")
        if name_del_con in self.dic_phone_book:
            del self.dic_phone_book[name_del_con]
            return "Ok , Contact Deleted Successfully"
        else:
            return f"Name {name_del_con} Has Not Been Found"

    def show_contact(self):

        return self.dic_phone_book

Phone_Book = Phone_Book()

while True:
    user = input("Please Select Phone Book Mode : (1) Add Contact | (2) Search Contact | (3) Delete Contact | (4) Show Contact | (5) Exit : ")
    if user == "1":
        print(Phone_Book.add_contact())

    elif user == "2":
        print(Phone_Book.search_contact())

    elif user == "3":
        print(Phone_Book.delete_contact())
    elif user == "4":
        print(Phone_Book.show_contact())
    elif user == "5":
        print("Ok , Bye")
        break
    else:
        print("Please Select Phone Book Mode")
        continue
