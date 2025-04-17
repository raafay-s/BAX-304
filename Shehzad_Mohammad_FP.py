# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:13:34 2024

@author: raafay
"""
#Author: Mohammad Raafay Shehzad
#Assignment Number & Name: Final project (Inventory management for a baking supply shop )
#Due Date: December 10th, 2024
#Program Description:
#%%
import Shehzad_Mohammad_FP_Classes

def process_inventory_file():
    inventory_list = []
    
    inventory_file = open('Inventory.txt', 'r')

    item_id = inventory_file.readline().strip()
    
    while item_id != '':
        item_id = inventory_file.readline().rstrip()
        name = inventory_file.readline().rstrip()
        stock = int(inventory_file.readline().rstrip())
        price = float(inventory_file.readline().rstrip())

        inventory_list.append(Shehzad_Mohammad_FP_Classes.Inventory(item_id, name, stock, price))
        
        item_id = inventory_file.readline().strip()
        
    inventory_file.close()

def print_inventory_menu(inventory_list):
    print("\nID\tName\t\t\tPrice\tStock")
    print("-" * 50)
    for item in inventory_list:
        # Using the __str__ method of the Inventory class to format the output
        print(item)

def get_item_id(inventory_list):
    while True:
        item_id = input("Enter the item ID to purchase/return (or 0 to finish): ").strip()
        
        # Check if the input is 0
        if item_id == "0":
            return "0"

        # Validate the ID
        for item in inventory_list:
            if item.get_id() == item_id:
                return item_id
        
        # If ID is invalid, notify the user
        print("Invalid item ID. Please try again.")


def handle_transaction(inventory_list, transaction_list):
    item_id = input("Enter the item ID to purchase/return (or 0 to finish): ")
    
    while item_id != "0":
        # Search for the item in inventory
        item_found = False
        for inventory_item in inventory_list:
            if inventory_item.get_id() == item_id:
                item = inventory_item
                item_found = True
        if not item_found:
            print("Invalid item ID. Please try again.")
        else:
            # Display item details
            print("Item found: " + item.get_name() +
                  " (Stock: " + str(item.get_stock()) +
                  ", Price: $" + format(item.get_price(), ".2f") + ")")
            action = input("Enter 'p' to purchase or 'r' to return: ").lower()
            quantity = int(input("Enter the quantity: "))

            if action == 'p':
                if quantity > 0 and quantity <= item.get_stock():
                    # Update inventory and store transaction
                    item.purchase(quantity)
                    transaction_list.append(Shehzad_Mohammad_FP_Classes.TransactionItem(
                        item.get_id(), item.get_name(), quantity, item.get_price()
                    ))
                    print("Purchased " + str(quantity) + " of " + item.get_name() + ".")
                else:
                    print("Invalid quantity or insufficient stock.")
            elif action == 'r':
                if quantity > 0:
                    # Update inventory and store transaction
                    item.restock(quantity)
                    transaction_list.append(Shehzad_Mohammad_FP_Classes.TransactionItem(item.get_id(), item.get_name(), -quantity, item.get_price()
))
                    print("Returned " + str(quantity) + " of " + item.get_name() + ".")
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid action. Please try again.")
                
        item_id = input("Enter the item ID to purchase/return: ")

    print("Transactions completed.")

def write_updated_inventory(filename, inventory_list):
    with open(filename, 'w') as file:
        for item in inventory_list:
            file.write(item.get_id() + '\n')
            file.write(item.get_name() + '\n')
            file.write(str(item.get_stock()) + '\n')
            file.write(format(item.get_price(), ".2f") + '\n')
    print("Updated inventory written to " + filename)


def print_invoice(transaction_list):
    if not transaction_list:
        print("No transactions to display. Thank you for visiting!")
        return

    print("\nInvoice:")
    print("ID\tName\t\tQuantity\tPrice\tTotal")
    print("-" * 50)

    total_cost = 0
    for transaction in transaction_list:
        cost = transaction.calc_cost()
        total_cost += cost
        print(transaction.get_id() + "\t" + transaction.get_name().ljust(20) +
              "\t" + str(transaction.get_quantity()) +
              "\t$" + format(transaction.get_price(), ".2f") +
              "\t$" + format(cost, ".2f"))

    # Calculate tax and grand total
    tax = total_cost * 0.085
    grand_total = total_cost + tax
    print("\nTotal Cost: $" + format(total_cost, ".2f"))
    print("Sales Tax (8.5%): $" + format(tax, ".2f"))
    print("Grand Total: $" + format(grand_total, ".2f"))


def main():
    # Step 1: Process inventory file
    inventory_list = process_inventory_file()

    # Step 2: Print the inventory menu
    print_inventory_menu(inventory_list)

    # Step 3: Initialize the transaction list
    transaction_list = []

    # Step 4: Handle transactions
    handle_transaction(inventory_list, transaction_list)

    # Step 5: Print invoice
    print_invoice(transaction_list)

    # Step 6: Write updated inventory to a file
    write_updated_inventory('UpdatedInventory.txt', inventory_list)

main()