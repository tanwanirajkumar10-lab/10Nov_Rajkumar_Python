'''Case Overview
You are a trainee Python developer at TechFix Solutions, a fast-growing gadget repair center. Currently, the team handles repair job records using sticky notes and phone calls. This leads to misplaced orders, confused billing, and delayed repairs.
The company has requested a Python-based console program, named FixTrack, that allows staff to track device repair orders and generate simple bills — using only core Python programming features.'''

orders = []

def show_menu():
    print(" Welcome To FixTrack ".center(50,"*"))
    print("1: Add New Device For Repair")
    print("2: View All Repair Orders")
    print("3: Generate Invoice")
    print("4: Update Existing Order")
    print("5: Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        cust_name = input("Enter Customer Name: ")
        dev_type = input("Enter Device Type: ")
        dev_issue = input("Enter Device Issue: ")
        due_date = input("Enter Due Date YYYY-MM-DD: ")

        orders.append({
            "cust_name": cust_name,
            "dev_type": dev_type,
            "dev_issue": dev_issue,
            "due_date": due_date,
            "repair_cost": 0.0,
            "parts_cost": 0.0,
            "tax": 0.0,
            "total_with_tax": 0.0
        })
        print("Order added successfully!")

    elif choice == "2":
        if len(orders) == 0:
            print("No orders to show".center(50, "*"))
        else:
            print("All Repair Orders".center(50, "*"))
            for index, item in enumerate(orders, start=1):
                print(f"Order No: {index}")
                print("Customer Name:", item["cust_name"])
                print("Device Type:", item["dev_type"])
                print("Device Issue:", item["dev_issue"])
                print("Due Date:", item["due_date"])
                print("Repair Cost:", item["repair_cost"])
                print("Parts Cost:", item["parts_cost"])
                print("Tax (5%):", item["tax"])
                print("Total Including Tax:", item["total_with_tax"])

    elif choice == "3":
        if len(orders) == 0:
            print("No orders available for invoice.".center(50, "*"))
        else:
            print("Generate Invoice".center(50, "*"))
            order_num = int(input("Enter order number to generate invoice: "))

            if order_num < 1 or order_num > len(orders):
                print("Invalid order number!")
            else:
                repair_fee = float(input("Enter Repair Cost: "))
                parts_fee = float(input("Enter Cost for Parts Replaced: "))

                item = orders[order_num - 1]
                item["repair_cost"] = repair_fee
                item["parts_cost"] = parts_fee

                subtotal = repair_fee + parts_fee
                item["tax"] = subtotal * 0.05
                item["total_with_tax"] = subtotal + item["tax"]

                print("Invoice".center(50, "*"))
                print("Customer Name:", item["cust_name"])
                print("Device Type:", item["dev_type"])
                print("Device Issue:", item["dev_issue"])
                print("Due Date:", item["due_date"])
                print("Repair Cost:", item["repair_cost"])
                print("Parts Cost:", item["parts_cost"])
                print("Tax (5%):", item["tax"])
                print("Total Including Tax:",item["total_with_tax"])

    elif choice == "4":
        if len(orders) == 0:
            print("No orders available to update.")
        else:
            print("Update Existing Order".center(50, "*"))
            order_num = int(input("Enter order number to update: "))

            if order_num < 1 or order_num > len(orders):
                print("Invalid order number!")
            else:
                order = orders[order_num - 1]
                print("Current order details:")
                print("1. Customer Name:", order["cust_name"])
                print("2. Device Type:", order["dev_type"])
                print("3. Device Issue:", order["dev_issue"])
                print("4. Due Date:", order["due_date"])
                print("5. Cancel Update")

                field_choice = input("Enter the number of the field you want to update:")

                if field_choice == "1":
                    order["cust_name"] = input("Enter new Customer Name:")
                elif field_choice == "2":
                    order["dev_type"] = input("Enter new Device Type:")
                elif field_choice == "3":
                    order["dev_issue"] = input("Enter new Device Issue:")
                elif field_choice == "4":
                    order["due_date"] = input("Enter new Due Date:")
                elif field_choice == "5":
                    print("Update canceled")
                else:
                    print("Invalid choice! No changes made")

                print("Order updated successfully!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice — please try again")