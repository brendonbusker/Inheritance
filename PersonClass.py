class Person:
    
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone


    def print_person(self):
        return f"Name: {self.__name}, Address: {self.__address}, Phone: {self.__phone}"


    
class Customer(Person):

    def __init__(self, name, address, phone, cust_num, mail_list):
        Person.__init__(self, name, address, phone)
        
        self.__cust_num = cust_num
        self.__mail_list = mail_list

    def print_person(self):
        return f"{Person.print_person(self)}, Cust Num: {self.__cust_num}, Mail List: {self.__mail_list}"
