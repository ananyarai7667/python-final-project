class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount, category):
        expense = {
            'description': description,
            'amount': amount,
            'category': category
        }
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
        else:
            print("List of Expenses:")
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. Description: {expense['description']}, Amount: ${expense['amount']}, Category: {expense['category']}")

    def total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total expenses: ${total}")

def main():
    expense_tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            expense_tracker.add_expense(description, amount, category)
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            expense_tracker.total_expenses()
        elif choice == '4':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
