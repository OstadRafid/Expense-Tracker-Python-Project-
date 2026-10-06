def Add_Expense(ExpenseID,Date,Catagory,Description,Amount):
    with open("Expense.txt","a") as File:
        File.write(f"ExpenseID -> {ExpenseID}\nDate-> {Date}\nCatagory-> {Catagory}\nDescription-> {Description}\nAmount-> {Amount}\n\n")
        File.close()

def view_expenses():
    with open("Expense.txt","r") as File:
        Content = File.read()
        print("-------------------------------")
        print("Details:")
        print(Content)
        print("-------------------------------")
        File.close()

def search_expense(ExpenseID):
    with open("Expense.txt","r") as File:
        content = File.read()

    Expenses = content.split("\n\n")

    for Expense in Expenses:
        if Expense.startswith(f"ExpenseID -> {ExpenseID}"):
            print(f"\nFound ExpenseID -> {ExpenseID}")
            print("--------------------------")
            print(Expense)
            print("--------------------------")
            return

    print("ExpenseID Not Found.")

def Update_Expense():
    ExpenseID_1 = int(input("Enter ExpenseID -> "))
    Choice = int(input("Select Options -> "))

    with open("Expense.txt", "r") as File:
        content = File.readlines()

    Found = False
    Current_ID = None

    for i in range(len(content)):

        if content[i].startswith("ExpenseID"):
            Current_ID = int(content[i].split("->")[1].strip())

        if Current_ID == ExpenseID_1:

            if Choice == 1:
                New_Date = input("Update Date -> ")
                content[i + 1] = "Date-> " + New_Date + "\n"
                Found = True
                break

            elif Choice == 2:
                Catagory_1 = input("Update Catagory -> ")
                content[i + 2] = "Catagory-> " + Catagory_1 + "\n"
                Found = True
                break

            elif Choice == 3:
                Description_1 = input("New Description -> ")
                content[i + 3] = "Description-> " + Description_1 + "\n"
                Found = True
                break

            elif Choice == 4:
                Amount_1 = int(input("New Amount -> "))
                content[i + 4] = "Amount-> " + str(Amount_1) + "\n"
                Found = True
                break

    with open("Expense.txt", "w") as File:
        File.writelines(content)

    if Found:
        print("Successfully Updated.")
    else:
        print("ExpenseID Not Found.")
        
def Delete_Expense(ExpenseID_1):
    with open("Expense.txt", "r") as File:
        content = File.readlines()

    New_Content = []
    i = 0
    Found = False

    while i < len(content):

        if content[i].startswith("ExpenseID"):
            Current_ID = int(content[i].split("->")[1].strip())

            if Current_ID == ExpenseID_1:
                Found = True
                i += 6
                continue

        New_Content.append(content[i])
        i += 1

    with open("Expense.txt", "w") as File:
        File.writelines(New_Content)

    if Found:
        print("Expense Deleted Successfully.")
    else:
        print("ExpenseID Not Found.")

def expense_summary():
    print("----------------------------------")
    print("Details:")
    with open("Expense.txt", "r") as File:
        content = File.readlines()
        File.close()

    Total_Expenses = 0
    Spending = 0
    Highest_Expense = 0
    Lowest_Expense = 0

    for i in range(len(content)):
        if content[i].startswith("ExpenseID"):
            Total_Expenses = Total_Expenses + 1

        if content[i].startswith("Amount->"):
            New = int(content[i].split("->")[1].strip())
            Spending = Spending + New
            
            if New > Highest_Expense:
                Highest_Expense = New

            if New < Highest_Expense:
                Lowest_Expense = New

    Avg = Spending /Total_Expenses

    print(f"Total_Expenses -> {Total_Expenses}")
    print(f"Total Spending -> {Spending}")
    print(f"Average Expense -> {Avg:.2f}")
    print(f"Height Expense -> {Highest_Expense}")
    print(f"Lowest Expense -> {Lowest_Expense}")

    print("-----------------------------------")

def Exit():
    exit()

while True:
    print("|-----------------------------------------------------|".center(108))
    print("|<<<========== Expense Tracker ==========>>>|".center(108))
    print()
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Expense Summary")
    print("7. Exit")
    print("|-----------------------------------------------------|".center(108))

    try:
        Take_Number = int(input("Chose The Options -> ").center(100))
        print()
        
        match Take_Number:

            case 1:
                try:
                    ExpenseID = int(input("ExpenseID : "))
                    Date = input("Date : ")
                    Catagory = input("Catagory : ")
                    Description = input("Description : ")
                    Amount = int(input("Amount : "))
                    
                    Add_Expense(ExpenseID,Date,Catagory,Description,Amount)
                    
                except Exception as File:
                    print(f"|Invalid Interrupt|{File}")
                finally:
                    print("Expense Added Successfully✅")

            case 2:
                view_expenses()

            case 3:
                
                ExpenseID_1 = int(input("Enter ExpenseID -> "))

                Found = 0
                
                with open("Expense.txt","r") as File:
                    Frist_Line = File.readline()
                    ExpenseID = int(Frist_Line.split("->")[1].strip())
                
                search_expense(ExpenseID_1)

            case 4:
                print("----------------------------------------------")
                print("<<<============ Update Expense ============>>>")
                print("1.Date")
                print("2.Category")
                print("3.Description")
                print("4.Amount")
                print("----------------------------------------------")

                Update_Expense()

            case 5:
                ExpenseID_1 = int(input("Enter ExpenseID -> "))
                Delete_Expense(ExpenseID_1)

            case 6:
                expense_summary()
            case 7:
                print("Thank You for Using Expense Tracker!")
                print("End of the Program.")
                Exit()

    except Exception as FILE:
        print(f"|Default|{FILE}")
"""
Developed By Rafid Al Mahmud.
Software Engineer.
Daffodil International Univarsity,DIU.
Contact: rezaulkhansha@gmail.com
"""