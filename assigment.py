classmate = {
    "ankit":"1234567890",
    "yash":"1234567891",
    "shashwat":"1234567892",
    "janya":"1234567893",
    "disha":"1234567894",
    "aarav":"1234567895",
    "haiya":"1234567896",
    "pallav":"1234567897",
    "gautam":"1234567898",
    "shivansh":"1234567899",
    "alok":"1234567810",
    "anupam":"1234567811",
    "rahul":"1234567812",
    "raj":"1234567813",
    "navya":"1234567814",
    "rohit":"1234567815",
    "vishal":"1234567816",
    "amar":"1234567817",
    "mayur":"1234567818",
    "parth":"1234567819",
    "ayush":"1234567820",
    }

print("1: for display all names and contact")
print("2: for searching contact")
print("3: for searching multiple contact")
ch = int(input("enter a choice(1,2,3): "))
if ch==1:
    for x,y in classmate.items():
        print(x,y)
elif ch==2:
    name = input("enter the name: ")
    print("Contact number is:",classmate[name])
elif ch==3:
    print("Enter end to exit the function")   
    for i in range(20):
        a=input("Enter the name: ")
        if(a=='end'):
            break
        else:
             print("Contact number is:",classmate[a])
        
else:
    print("invalid number!")
    

    