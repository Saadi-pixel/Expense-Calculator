import csv
from tabulate import tabulate
filename="expenses.csv"
def add_expense():
    category=input("Enter the Category: ")
    item=input("Enter the Item name: ")
    
    date=input("Enter the date: ")
    while True:
        try:
            amount=int(input(f"Enter the amount of {item} :"))
            break
        except ValueError:
            print("Enter the amount in integers...")
    with open(filename,"a",newline="")     as file:
        writer=csv.writer(file) 
        writer.writerow([category,item,date,amount])
    print("Expense Added successfully")  
def show_expenses():
    try:

        with open(filename,"r")as file:
            rows=list(csv.reader(file))
            headers=("Category","Item","Date","Amount")    
            if rows:
                    print(tabulate(rows,headers=headers,tablefmt="fancy_grid"))
            else:
                   print("No such record found") 
    except FileNotFoundError:
        print("No expense record found yet...")              
def search_expense():
    found = False
    search_entity = input("Enter the category to search for : ")  
    matching_rows = []
    try:
    
        with open(filename, "r") as file:
            reader = csv.reader(file)
            headers = ("Category", "Item", "Date", "Amount")
        
            for row in reader:
                if row:
                    if row[0] == search_entity:
                        matching_rows.append(row)
                        found = True
                    
        if found:
            print(tabulate(matching_rows, headers=headers, tablefmt="fancy_grid"))
        else:
            print(f"No record found for {search_entity} category")                
    except FileNotFoundError:
        print("No expense records found yet.")

def calculate_total():
    total_amount=0
    try:
        with open (filename,"r") as file:
            reader=csv.reader(file)
            for  row in reader:
                if row:
                    total_amount+=int(row[3]) 
            print(f"Your Total spendings are: {total_amount}") 
    except FileNotFoundError:
        print("No expense records found yet.")        
def calculate_categorywise_spendings():
    total=0
    search_category=input("Enter the category to calculate total of particular category: ")
    found = False
    try:
        with open (filename,"r") as file:
            reader=csv.reader(file)
            for row in reader:
                if row:
                    if search_category==row[0]:
                        total+=int(row[3])
                        found=True
        if found==False:
            print("Record not found")
        else:
            print(f"Total spendings for {search_category} are {total}")                    
    except FileNotFoundError:
        print("No expense records found yet.")
def main():
    while True:
        
        print("----------------------------------------------------------")
        print("         DAILY AND MONTHLY EXPENSE CALCULATOR             ")
        print("----------------------------------------------------------")
        print("     1.Add Expense       ")
        print("     2.Show All Expenses ")
        print("     3.Search Expenses of particular Category")
        print("     4.Calculate Total Spendings  ")
        print("     5.Calculate Spendings Categorywise ")
        print("     6.Exit system ")
        choice=input("Choose any button from 1 to 6 according to your need: ")
        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expenses()
        elif choice=="3":
            search_expense()       
        elif choice=="4":
            calculate_total()
        elif choice=="5":
            calculate_categorywise_spendings()
        elif choice=="6":
            print("Thank you , you are exiting the system.....") 
            break  
        else:
            print("Error[ please enter only 1 to 7 only.. ]")       

if __name__ == "__main__" :
    main()
