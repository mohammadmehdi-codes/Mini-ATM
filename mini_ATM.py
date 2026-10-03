pin = "1111" #demo PIN
balance = 1000  #demo Balance
total_history = []
def check_balance():
    print("Balance: ",balance )

def withdraw():
    global balance
    try:
        withdraw_amount = int(input("Enter amount: "))
    except ValueError:
        print("Invalid input, please enter amount")
        return
    if withdraw_amount <= 0:
        print("Only positive amounts can be withdrawn")
    else:
        if withdraw_amount > balance:
            print("Insufficient balance.")
        else:
            balance -= withdraw_amount
            total_history.append(f"Withdraw: {withdraw_amount} | Balance: {balance}")
            print("Please collect your cash.")
            print("Your remaining balance: ",balance)

def deposit():
    global balance
    try:
        deposit_amount = int(input("Enter amount: "))
    except ValueError:
        print("Invalid input, please enter amount")
        return    
    if deposit_amount <= 0:
        print("Only positive amounts can be deposited")
    else:
        balance += deposit_amount
        total_history.append(f"Deposit: {deposit_amount} | Balance: {balance}")
        print("Amount deposited successfully")
        print("Your current balance: ",balance)

def change_pin():
    global pin
    old_pin = input("Enter old PIN for verification:")
    if old_pin == pin:
        new_pin = input("Enter New 4-digit PIN: ")
    else:
        print("Incorrect PIN entered")
        return
    if pin == new_pin:
        print("Failed. New PIN should not be the same as the old PIN.")
    else:
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Try again. Please enter a 4-digit PIN.")

def transaction_history():
    if len(total_history) == 0:
        print("No transaction history found.")
    else:
        for i, history in enumerate(total_history, start=1):
            print(i,":", history)

print("--------Welcome to the Mini ATM-----------")
attempts = 2
while attempts >= 0:
    entered_pin = input("Please enter your 4 digit PIN: ")
    if pin != entered_pin:
        print("Incorrect PIN ",attempts,"attempts left")
        attempts -= 1
        if attempts == -1:
            print("All attempts failed. Access denied.")
        continue
    else:
        while True:
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")
            try:
                choice = int(input("Choose an option (1-6):"))
            except ValueError:
                print("Invalid input. Please choose an option from 1 to 6.")
                continue
            if choice == 1:
                check_balance()
    
            elif choice == 2:
                withdraw()
                
            elif choice == 3:
                deposit()
                
            elif choice == 4: 
                change_pin()
            elif choice == 5:
                transaction_history()               
                
            elif choice == 6:
                print("Thank you for using the Mini ATM.") 
                break
            else:
                print("Invalid input.")           
               