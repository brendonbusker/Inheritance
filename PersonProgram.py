import PersonClass as p

#jj = p.Person("jj", "321 demo street", "420-699-6969")
#zane = p.Customer("zane", "123 test street", "420-420-4201", 12, True)

name = "JJ"
address = "321 demo street"
phone = "123-456-7891"
cust_num = 1234
on_list = False

person = p.Person(name, address, phone)
customer = p.Customer(name, address, phone, cust_num, on_list)

#Print Person object
person.print_person()

print()

#Print Customer Object
customer.print_person()