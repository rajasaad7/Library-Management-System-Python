def getDate():
    import datetime
    now=datetime.datetime.now
    #print("Date: ",now().date())
    return str(now().date())

def getTime():
    import datetime
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())


global bookname
global authorname
global quantity
global cost
bookname = []
authorname = []
quantity = []
cost = []
with open("Stock.txt", "r") as f:
    lines = f.readlines()
    lines = [x.strip('\n') for x in lines]
    for i in range(len(lines)):
        ind = 0
        for a in lines[i].split(','):
            if (ind == 0):
                bookname.append(a)
            elif (ind == 1):
                authorname.append(a)
            elif (ind == 2):
                quantity.append(a)
            elif (ind == 3):
                cost.append(a.strip("$"))
            ind += 1
    f.close()
def signup():
    usern = input("Enter your username ")
    passw = input("Enter your password ")
    to = open("users.txt", "a")
    to.write("\n"+usern+","+passw)
    to.close()
    
def login():

    user = input("Username: ")
    passw = input("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split(",")
        if (user in us) and (passw in pw):
            print ("Login successful!")
            return True
    print ("Wrong username/password")
    exit()
    return False
asd = input("Press 1 for login and 2 for sign up")
if(asd == "1"):
    login()
elif(asd == "2"):
    signup()
else:
    print("Enter valid Input")
    exit()
def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Add a Book")
        print("Enter 3. To Borrow a book")
        print("Enter 4. To return a book")
        print("Enter 5. Search a book")
        print("Enter 6. To exit")
        try:
            a=int(input("Select a choice from 1-6: "))
            print()
            if(a==1):
                with open("Stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
                    f.close()
            elif(a==2):
                name = input("Enter Name of the Book ")
                author = input("Enter Name of the Author ")
                quant = input("Enter Quantity ")
                price = input("Enter Cost per Book ")

                bro = open("Stock.txt", "a")
                bro.write("\n"+name+","+author+","+quant+",$"+price)
                bro.close()

            elif(a==3):

                def borrowBook():
                    success = False
                    while (True):
                        firstName = input("Enter the name of the borrower: ")
                        if firstName.isalpha():
                            break
                        print("please input alphabet from A-Z")
                    while (True):
                        lastName = input("Enter the last name of the borrower: ")
                        if lastName.isalpha():
                            break
                        print("please input alphabet from A-Z")

                    t = "Borrow-" + firstName + ".txt"
                    with open(t, "w+") as f:
                        f.write("               Library Management System  \n")
                        f.write("                   Borrowed By: " + firstName + " " + lastName + "\n")
                        f.write("    Date: " + getDate() + "    Time:" +getTime() + "\n\n")
                        f.write("S.N. \t\t Bookname \t      Authorname \n")
                        f.close()

                    while success == False:
                        print("Please select a option below:")
                        for i in range(len(bookname)):
                            print("Enter", i, "to borrow book", bookname[i])

                        try:
                            a = int(input())
                            try:
                                if (int(quantity[a]) > 0):
                                    print("Book is available")
                                    with open(t, "a") as f:
                                        f.write("1. \t\t" + bookname[a] + "\t\t  " + authorname[
                                            a] + "\n")
                                    f.close()

                                    quantity[a] = int(quantity[a]) - 1
                                    with open("Stock.txt", "w+") as f:
                                        for i in range(3):
                                            f.write(bookname[i] + "," + authorname[i] + "," + str(
                                                quantity[i]) + "," + "$" + cost[i] + "\n")
                                    f.close()
                                    # multiple book borrowing code
                                    loop = True
                                    count = 1
                                    while loop == True:
                                        choice = str(input(
                                            "Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                                        if (choice.upper() == "Y"):
                                            count = count + 1
                                            print("Please select an option below:")
                                            for i in range(len(bookname)):
                                                print("Enter", i, "to borrow book", bookname[i])
                                            a = int(input())
                                            if (int(quantity[a]) > 0):
                                                print("Book is available")
                                                with open(t, "a") as f:
                                                    f.write(str(count) + ". \t\t" + bookname[a] + "\t\t  " +
                                                            authorname[a] + "\n")
                                                f.close()
                                                quantity[a] = int(quantity[a]) - 1
                                                with open("Stock.txt", "w+") as f:
                                                    for i in range(3):
                                                        f.write(bookname[i] + "," + authorname[
                                                            i] + "," + str(quantity[i]) + "," + "$" +
                                                                cost[i] + "\n")
                                                        success = False
                                                f.close()
                                            else:
                                                loop = False
                                                break
                                        elif (choice.upper() == "N"):
                                            print("Thank you for borrowing books from us. ")
                                            print("")
                                            loop = False
                                            success = True
                                        else:
                                            print("Please choose as instructed")

                                else:
                                    print("Book is not available")
                                    break
                                    success = False
                            except IndexError:
                                print("")
                                print("Please choose book acording to their number.")
                        except ValueError:
                            print("")
                            print("Please choose as suggested.")
                borrowBook()
            elif(a==4):
                def returnBook():
                    name = input("Enter name of borrower: ")
                    a = "Borrow-" + name + ".txt"
                    try:
                        with open(a, "r") as f:
                            lines = f.readlines()
                            lines = [a.strip("$") for a in lines]
                        f.close()

                        with open(a, "r") as f:
                            data = f.read()
                            print(data)
                        f.close()
                    except:
                        print("The borrower name is incorrect")
                        returnBook()

                    b = "Return-" + name + ".txt"
                    with open(b, "w+")as f:
                        f.write("                Library Management System \n")
                        f.write("                   Returned By: " + name + "\n")
                        f.write("    Date: " + getDate() + "    Time:" +getTime() + "\n\n")
                        f.write("S.N.\t\tBookname\t\tCost\n")
                        f.close()
                    total = 0.0
                    for i in range(3):
                        if bookname[i] in data:
                            with open(b, "a") as f:
                                f.write(
                                    str(i + 1) + "\t\t" + bookname[i] + "\t\t$" + cost[i] + "\n")
                                quantity[i] = int(quantity[i]) + 1
                            total += float(cost[i])
                            f.close()

                    print("\t\t\t\t\t\t\t" + "$" + str(total))
                    print("Is the book return date expired?")
                    print("Press Y for Yes and N for No")
                    stat = input()
                    if (stat.upper() == "Y"):
                        print("By how many days was the book returned late?")
                        day = int(input())
                        fine = 2 * day
                        with open(b, "a")as f:
                            f.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
                        total = total + fine
                        f.close()
                    print("Final Total: " + "$" + str(total))
                    with open(b, "a")as f:
                        f.write("\t\t\t\t\tTotal: $" + str(total))
                    f.close()
                    with open("Stock.txt", "w+") as f:
                        for i in range(4):
                            f.write(bookname[i] + "," + authorname[i] + "," + str(
                                quantity[i]) + "," + "$" + cost[i] + "\n")
                    f.close()
                returnBook()
            elif(a==5):
                def searching(blabla):
                    with open('Stock.txt') as f:
                        datafile = f.readlines()
                    found = False
                    f.close()
                    for line in datafile:
                        if blabla in line:
                            print(line)
                            return True
                    return False
                word = input()
                searching(word)
            elif(a == 6):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
