def main():
    print ("Welcome to Supermarket Billing System")
    # Store grand total sales across all customers
    total_bill = 0.0
    
    while True:
        # 1. Setup and Variable Initialization for the current customer
        customer_total = 0.0
        discount = 0.0
        final_bill = 0.0
        
        # Parallel arrays (lists) with space for up to 100 items
        product_list = ["" for _ in range(100)]
        quantity_list = [0 for _ in range(100)]
        price_list = [0.0 for _ in range(100)]
        
        # 'i' acts as our primary array index pointer
        i = 0
        
        # 2. The Customer Purchase Loop (Data Input)
        while True:
            # Capture data entry inputs
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            price_per_unit = float(input("Enter price per unit: "))
            
            # Store values into our parallel lists at position [i]
            product_list[i] = product_name
            quantity_list[i] = quantity
            price_list[i] = price_per_unit
            
            # Calculate item totals and accumulate into the subtotal
            item_total = quantity * price_per_unit
            customer_total = customer_total + item_total
            
            # Move the pointer to the next array slot
            i = i + 1
            
            # Check if there are more items for this customer
            more_items = input("Any more items? (Yes/No): ").strip().lower()
            if more_items != "yes":
                break  # Breaks the data capture loop
                
        # 3. The 10% Promotional Discount Check (Decision Structure)
        if customer_total > 500:
            discount = customer_total * (10 / 100)
            final_bill = customer_total - discount
        else:
            discount = 0.0
            final_bill = customer_total
            
        # Add current transaction into the store ledger
        total_bill = total_bill + final_bill
        
        # 4. Structured Receipt Generation Loop (The part we fixed!)
        print("\n--- RECEIPT ---")
        item_position = 0
        
        while item_position < i:
            # Displays the receipt line-by-line using sequential printing
            print(f"Product: {product_list[item_position]}")
            print(f" | Qty: {quantity_list[item_position]}")
            print(f" | Price: Le {price_list[item_position]}")
            
            # Step the loop counter index forward
            item_position = item_position + 1
            
        # Print final financial summaries for the shopper
        print(f"\nSubTotal = Le {customer_total:.2f}")
        print(f"Discount = Le {discount:.2f}")
        print(f"FinalBill = Le {final_bill:.2f}")
        print("-" * 15)
        
        # 5. Master Reset Frame / Next Customer Check
        any_more_customers = input("Any more customers? (Yes/No): ").strip().lower()
        if any_more_customers != "yes":
            break  # Shuts down the master store loop

    print(f"\nSystem Terminated. Grand Total Store Sales Today: Le {total_bill:.2f}")

# This starts the program execution
if __name__ == "__main__":
    main()
