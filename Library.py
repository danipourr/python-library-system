import os
import json

class Library:
    def __init__(self):
        self.dict_library = {}
        self.load_data()

    def add_book(self):
        name_book = input('Please Write The Name Of Book :')
        author = input('Please Write The Author`s Name :')
        self.dict_library[name_book] = author
        self.save_data()
        return 'Ok , Added Successfully'
        
    def delete_book(self):
        name_del = input('Please Write Name For Delete :')
        if name_del not in self.dict_library:
            return'This Book Not Found!!'
        elif name_del in self.dict_library:
            del(self.dict_library[name_del])
            self.save_data()
            return 'Deleted !!'
        
    def show_lib(self):
        if not self.dict_library:
            return("Library is Empty!")
            
        print('=========== List Library ===========')
        for book , auth in self.dict_library.items():
            print(f'The Name Book : {book}') 
            print(f'The Name Author : {auth}')
    
    def search_name(self):
        name_sear = input('Please Write The Book Name For Search :')

        for book, author in self.dict_library.items():
            if book == name_sear:
                return f"Book: {book} | Author: {author}"

        return "Name Not Found!!"
        
        
    def search_author(self):
            author_sear = input('Please Write The Author Name For Search :')

            for book, author in self.dict_library.items():
                if author == author_sear:
                    return f"Book: {book} | Author: {author}"
                
            return "Author Not Found!!"
    
    def save_data(self):
        with open ('Library_Save.json' , 'w') as file:
            json.dump(self.dict_library , file)
    
    def load_data(self):
        if os.path.exists("Library_Save.json"):
            with open ('Library_Save.json' , 'r') as file:
                self.dict_library =   json.load(file)  

    def edit_book(self):
        name_for_edit = input('Please Write Name`s Book For Edit :')
        if name_for_edit in self.dict_library:
            del(self.dict_library[name_for_edit])
            new_name = input('Please Write New Name :')
            new_author = input('Please Write New Author : ')
            self.dict_library[new_name] = new_author
            self.save_data()
            return 'Ok , Edited Successfully'
        else:
            return "Book Not Found!!"




library_system = Library('')
while True:
    menu_choice = input('Please Select : 1 (Add Book) | 2 (Delete Book) | 3 (Show Library) | 4 (Search By Name) | 5 (Search By Author) | 6 (Edit Book) | 7 (Exit) :')
    if menu_choice =="7":
        print('Have a Nice Day😊 \n GoodBye')
        break
    if menu_choice == '1':
        print(library_system.add_book())  
            
    if menu_choice == '2':
        print(library_system.delete_book())

    if menu_choice == '3':
        library_system.show_lib()

    if menu_choice == '4':
        print(library_system.search_name())

    if menu_choice == '5':
        print(library_system.search_author())

    if menu_choice == '6':
        print(library_system.edit_book())