products = []
f = open("jalase 7/4-1database.txt", "r")
def read_text_from_file():
    f = open("jalase 7/4-1database.txt", "r")
    for line in f:
        result = line.split(",") 
        my_dict = {"id":result[0], "name":result[1], "price":result[2], "count":result[3]}
        products.append(my_dict)


def add():
    yd = input("enter id : ")
    name = input("enter name : ")
    price = input("enter price : ")
    count = input("enter count : ")

    new_product = {"id":yd, "name":name, "price":price, "count":count}
    products.append(new_product)
    f.write(yd, ",", name, ",", price, ",", count, "\n")
    print("New product has been successfully added.")

def delete():
    code = int(input("Enter item index : "))
    #products.delete(code)
    print("Selected product has been successfully removed.")


def edit(): 
    num = input("enter id for edit : ")
    for product["id"] in products :
        while True:
            if product["id"] == num:
                print("1-name")
                print("2-price")
                print("3-count")
                print("0-exit")

                op = int(input("enter your choice: "))
                if op == 1:
                    new_name = input("Enter new name: ")
                    product["name"] = new_name
                    print("successfully edited.")

                elif op == 2:
                    new_price = input("Enter the new price:")
                    product["price"] = new_price
                    print("successfully edited.")

                elif op == 3:
                    new_quantity = input("Enter the new count:")
                    product["quantity"] = new_quantity
                    print("successfully edited.")
                
                elif op == 0:
                    break

def search():
    op = input("enter your keyword : ")
    for product in products :
        if product["id"] or product["name"] == op :
            print(product)
            break
        else:
            print("not found!!!")

def show_list():
    print("id \t name \t price \t count")
    for product in products:
        print(product["id"], "\t", product["name"], "\t", product["price"], "\t", product["count"])


def buy():
    factor = []
    buy = 0
    while True:
        print("yes or no :")
        op = input("Would you want to make a purchase? ")
        if op == "yes":
            select_id = input("enter item id: ")
            for product in products :
                while True:
                    if product["id"] == select_id:
                        co = int(input("Enter your count: "))
                        buy += co*int(product["price"])
                        if int(product["count"]) >= co :
                            ad = {product["name"], str(co)}
                            factor.append(ad)
                            product["count"] = str(int(product["count"])-co)
                            break
                        elif int(product['count']) < co :
                            print("not available!!!")
                            break
            else:
                print("not found!!!")
                break
        elif op == "no":
            print("your factor :")
            for item in factor:
                print(item)
            print("cost is: ",buy)
            break
        

def show_menu():
    print("1- add")
    print("2- delete")
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
        show_list()
        delete()

    if choice == 3:
        show_list()
        edit()

    if choice == 4:
        search()

    if choice == 5:
        show_list()

    if choice == 6:
        show_list()
        buy()

    if choice == 7:
        f.close()
        exit(0)
        break

