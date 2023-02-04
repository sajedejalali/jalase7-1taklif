products = []
def read_text_from_file():
    f = open("jalase 7/4-1database.txt", "r")
    for line in f:
        result = line.split(",") 
        my_dict = {"id":result[0], "name":result[1], "price":result[2], "count":result[3]}
        products.append(my_dict)


def add():
    id = input("enter id : ")
    name = input("enter name : ")
    price = input("enter price : ")
    count = input("enter count : ")

    new_product = {"id":id, "name":name, "price":price, "count":count}
    products.append(new_product)

def delet():
    read_text_from_file()
    num = int(input("enter id : "))
    id = result[0]
    name = result[1]
    price = result[2]
    count = result[3]
    id_list = {result[0], result[1], result[2], result[3]}
    f.write(id_list)


def edit(): 
    read_text_from_file()
    f = open("jalase 7/4-1database.txt", "w")
    for line in f:
        result = line[0]
        num = int(input("enter id : "))
        if num == line[0] : 
            print("1 - name")
            print("2 - price")
            print("3 - count")
            op = input("enter your choice : ")
            if op == "1":
                name = input("enter name : ")
                products.write(name)

            if op == "2":
                price = int(input("enter price : "))
                products.write(price)

            if op == "3":
                count = int(input("enter count"))
                products.write(count)
    print("operation successfully completed!!!")
            

            

def search():
    pass

def show_list():
    print("id \t name \t price \t count")
    for product in products:
        print(product["id"], "\t", product["name"], "\t", product["price"], "\t", product["count"])


def buy():
    read_text_from_file()
    buy = 0
    while True:
        num = int(input("enter id :"))
        f = open("jalase 7/4-1database.txt", "a")
        for line in f :
            result = line
            if num == result[0] :
                if result[3] == 0:
                    print("inventory is not enough!!!")
                if result[3] > 0 :
                    op = int(input("enter the desired amount:"))
                    buy += op
                    result[3]-= op
                if result[3] < num :
                    print("inventory is not enough!!!")
                price = num*result[2]
                faktor = {result[1]: price}
                print(faktor)
                opp = input("c for continue & e for exit")
                if opp == "c":
                    continue
                if opp == "e":
                    break
                
        




def write_to_database():
    pass

def show_menu():
    print("1- add")
    print("2- delet")
    print("3- edit")
    print("4- search")
    print("5- show list")
    print("6- buy")
    print("7- exit")
    
while True :
    read_text_from_file()
    show_menu()
    choice = int(input("enter your choice: "))

    if choice == 1:
        add()
        

    if choice == 2:
        delet()

    if choice == 3:
        edit()
        

    if choice == 4:
        search()

    if choice == 5:
        show_list()

    if choice == 6:
        buy()

    if choice == 7:
        write_to_database()
        exit(0)
        break

