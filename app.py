from db import expenses
from bson import ObjectId

def add_expense():
    amount = float(input("Enter the amount: "))
    if amount<=0:
        print("Amount should be greater than 0")
    category = input("Enter the category: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    expenses.insert_one(expense)
    print("Expense added successfully")

def delete_expense():
    for expense in expenses.find():
        print(f"{expense['_id']} : {expense['description']} - {expense['amount']} on {expense['date']}")
    expenseid = input("enter the id to delete: ")
    expenses.delete_one({"_id": ObjectId(expenseid)})
    print("Expense deleted successfully")

def view_expense():
    
    for expense in expenses.find():
        print(f"{expense['_id']} : {expense['description']} - {expense['category']} - {expense['amount']} on {expense['date']}")
    print("Expenses displayed successfully")

def update_expense():
    expenseid = input("enter the id to update: ")
    amount = float(input("Enter the new amount: "))

    expenses.update_one({
        "_id": ObjectId(expenseid)},
        {"$set":{"amount": amount}}
    )

    print("Successfully updated the expense")

def category_report():
    result = expenses.aggregate([
        {
            "$group": {
                "_id": "$category",
                "total": {"$sum": "$amount"}
            }
        },
        {
            "$sort": {"total": 1}
        }
    ])

    print("\nCategory-wise Report")
    for item in result:
        print(f"{item['_id']} : ₹{item['total']}")


if __name__ == "__main__":
    print("Welcome to the Expense Tracker!")
    while True:
        print("1.Add expense")
        print("2.Delete Expense")
        print("3.View expenses")
        print("4.Update expense")
        print("5.category_report()")
        print("6.Exit")
        try:
            choice = int(input("Enter the number of your choice: "))
        except ValueError:
            print("Invalid choice")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            delete_expense()
        elif choice == 3:
            view_expense()
        elif choice == 4:
            update_expense()
        elif choice == 5:
            category_report()
        elif choice == 6:
            print("Exit")
            break