import json
from datetime import datetime

#file to store expense

DATA_FILE = "expense.json"

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_data()
        
    def load_data(self):
        try:
            with open(DATA_FILE,"r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    def save_data(self):
          with open(DATA_FILE,"w") as f:
              json.dump(self.expenses,f,indent=4)
    def add_expense(self,amount,category,note=""):
        expense ={
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        }     
        self.expenses.append(expense)
        self.save_data()     
        print(f" Added {amount} in {category} {note}")
        
    def view_expenses(self):
               if not self.expenses:
                   print("NO expenses recorded yet .")
                   return
               for i,exp in enumerate(self.expenses,start=1):
                    print(f"{i}. {exp['date']} - {exp['category'] } - ${exp['amount']} ({exp['note']}) ")
    def summary(self):
        if not self.expenses:
            print("No data to summarize.")
            return
        totals ={}
        for exp in self.expenses:
            totals[exp['category']] = totals.get(exp['category'], 0) + exp['amount']
            print("\n---Expense Summary ---")
            for cat,total in totals.items():
                print(f"{cat}: ${total}")    
    
    
    #main program
tracker = ExpenseTracker()
while True:
        print("\n--- Expense Tracker Menu ---")
        print("1.Add Expense")
        print("2.View Expense")
        print("3.Summary")
        print("4.Exit")
        
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (Food,Travel,etc..): ")
                note = input("Optional note: ")
                tracker.add_expense(amount,category,note)
            except ValueError:
                print("Invalid amount.Try again.")
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. please enter 1-4.")
                        
                   
                                         
                    