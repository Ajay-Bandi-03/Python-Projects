#Interactive Periodic Table Application
elements = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "group": "Non-metal"},
    "He": {"name": "Helium", "atomic_number": 2, "group": "Noble gas"},
    "Li": {"name": "Lithium", "atomic_number": 3, "group": "Alkali metal"},
    "O": {"name": "Oxygen", "atomic_number": 8, "group": "Non-metal"},
    "Fe": {"name": "Iron", "atomic_number": 26, "group": "Transition metal"},
    # Add more elements as needed
}

print("Welcome to the Interactive Periodic Table!")
while True:
    query = input("Enter the symbol of an element (or type 'exit' to quit): ").strip()
    if query.lower() == "exit":
        print("Thank you for using the Interactive Periodic Table. Goodbye!")
        break
    elif query in elements:
        info = elements[query]
        print(f"Name: {info['name']}, Atomic Number: {info['atomic_number']}, Group: {info['group']}")
    else:
        print("Element not found. Please try again.")
