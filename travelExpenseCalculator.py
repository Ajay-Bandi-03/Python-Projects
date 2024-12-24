class TravelExpenseCalculator:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        """Add an expense to a category."""
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def total_expense(self):
        """Calculate the total travel expenses."""
        return sum(self.expenses.values())

    def display_expenses(self):
        """Display all expenses by category."""
        print("\nTravel Expenses:")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount:.2f}")
        print(f"\nTotal: ${self.total_expense():.2f}")

if __name__ == "__main__":
    print("Travel Expense Calculator")
    calculator = TravelExpenseCalculator()

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter expense category (e.g., Transportation, Food, Lodging): ").capitalize()
            try:
                amount = float(input(f"Enter the amount for {category}: $"))
                calculator.add_expense(category, amount)
                print(f"Added ${amount:.2f} to {category}.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

        elif choice == "2":
            calculator.display_expenses()

        elif choice == "3":
            print("Exiting the Travel Expense Calculator. Safe travels!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
