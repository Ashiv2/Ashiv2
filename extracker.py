# Initialize variables
categories = ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other']
expenses = {category: 0 for category in categories}
total_expenses = 0

def add_expense(category, amount):
    global total_expenses
    if category in expenses:
        expenses[category] += amount
        total_expenses += amount
        print(f"Added ${amount:.2f} to {category}.")
    else:
        print("Invalid category. Please choose from: Food, Transport, Entertainment, Utilities, Other.")

def show_summary():
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ${total_expenses:.2f}")
    if total_expenses > 0:
        for category, amount in expenses.items():
            percentage = (amount / total_expenses) * 100
            print(f"{category}: ${amount:.2f} ({percentage:.2f}%)")
    else:
        print("No expenses recorded.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. Show Summary")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            category = input("Enter the category (Food, Transport, Entertainment, Utilities, Other): ")
            try:
                amount = float(input("Enter the amount: "))
                add_expense(category, amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        elif choice == '2':
            show_summary()
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()