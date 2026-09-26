correct_pin = "9999"
balance = 25000

def check_pin():
    attempts = 3
    while attempts > 0:
        entered_pin = input("PIN Number: ").strip()

        if len(entered_pin) != 4 or not entered_pin.isdigit():
            attempts -= 1
            print("Please Enter a valid PIN")
            continue

        if entered_pin == correct_pin:
            print("Welcome User!")
            return True
        else:
            attempts -= 1
            print(f"Please Enter a valid PIN. Attempts Remaning {attempts}")

    print("Too many attempts. Exiting...")
    return False

def show_menu():
    print("---- ATM MENU ----")
    print("1. Check Balance \n2. Deposit Money \n3. Withdraw Money \n4. Exit")

def main():
    global balance

    print("Welcome to Simple ATM Simulator")

    if not check_pin():
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                print("Your current balance is: ", balance)
            case "2":
                try:
                    amount = float(input("Enter amount to deposit: "))
                except ValueError:
                    print("Please Enter a valid amount")
                    continue
                if amount <= 0:
                    print("Deposit Amount should be greater than 0")
                else:
                    balance += amount
                    print("Your amount has been deposited to your account.")
                    print("Your current balance is: ", balance)

            case "3":
                try:
                    amount = float(input("Enter amount to withdraw: "))
                except ValueError:
                    print("Please Enter a valid amount")
                    continue

                if amount <= 0:
                    print("Withdrawal Amount should be greater than 0")
                elif amount > balance:
                    print("Insufficient Funds!")
                else:
                    balance -= amount
                    print("Amount has been withdrawn from your account successfully.")

            case "4":
                print("Exiting...")
                print("THANK YOU FOR USING ATM SIMULATOR")
                break

            case _:
                print("Invalid Option. Choose a correct one.")

if __name__ == "__main__":
    main()