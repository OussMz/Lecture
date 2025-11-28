from collections import defaultdict
expense_records = []
category_totals = defaultdict(float)
unique_categories = set()
overall_stats = defaultdict(float)

def data_entry():
    num_of_expenses = input("Enter number of expenses to record (5-7): ")
    while not num_of_expenses.isdigit() or not (3 <= int(num_of_expenses) <= 7):
        num_of_expenses = input("Invalid input. Please enter a number between 5 and 7: ")
    num_of_expenses = int(num_of_expenses)
    for i in range(num_of_expenses):
        category = input(f"Enter expense {i+1} category: ")
        amount = input(f"Enter expense {i+1} amount: ")
        while not amount.replace('.', '', 1).isdigit():
            amount = input("Invalid amount. Please enter a numeric value: ")
        amount = float(amount)
        date = input(f"Enter expense {i+1} date (YYYY-MM-DD): ")
        expense_records.append((category, amount, date))
        print("\n\n")
    overall_stats["highest_expense"] = {"amount": 0, "category": "", "date": ""}
    overall_stats["lowest_expense"] = {"amount": 0, "category": "", "date": ""}
    for category, amount, date in expense_records:
        if category not in unique_categories:
            unique_categories.add(category)
        category_totals[category] += amount
        overall_stats["total_spending"] += amount
        if amount > overall_stats["highest_expense"]["amount"]:
            overall_stats["highest_expense"]["amount"] = amount
            overall_stats["highest_expense"]["category"] = category
            overall_stats["highest_expense"]["date"] = date
        if overall_stats["lowest_expense"]["amount"] == 0 or amount < overall_stats["lowest_expense"]["amount"]:
            overall_stats["highest_expense"]["amount"] = amount
            overall_stats["highest_expense"]["category"] = category
            overall_stats["highest_expense"]["date"] = date
    overall_stats["average_expense"] = overall_stats["total_spending"] / num_of_expenses

def display_results():
    print("=== PERSONAL EXPENSE TRACKER ===")
    data_entry()
    print("=== OVERALL SPENDING SUMMARY ===")
    print(f"Total Spending: ${overall_stats["total_spending"]:.2f}")
    print(f"Average Expense: ${overall_stats["average_expense"]:.2f}")
    print(f"Highest Expesne: ${overall_stats["highest_expense"]["amount"]:.2f} (category: {overall_stats["highest_expense"]["category"]}, date: {overall_stats["highest_expense"]["date"]})")
    print(f"Lowest Expense: ${overall_stats["lowest_expense"]["amount"]:.2f} (category: {overall_stats["lowest_expense"]["category"]}, date: {overall_stats["lowest_expense"]["date"]})")
    print("\n\n=== UNIQUE CATEGORIES SPENT ON ===")
    print(unique_categories)
    print("Total unique categories: " +  str(len(unique_categories)), end="\n\n")
    print("=== SPENDING BY CATEGORY ===")
    for category, total in category_totals.items():
        print(f"Category: {category} | Total Spent: ${total:.2f}")
display_results()
