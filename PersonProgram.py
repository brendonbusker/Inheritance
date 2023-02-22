import PersonClass as p

jj = p.Person("jj", "321 demo street", "420-699-6969")
zane = p.Customer("zane", "123 test street", "420-420-4201", 12, True)

#Print Person object
print(jj.print_person())

#Print Customer Object
print(zane.print_person())