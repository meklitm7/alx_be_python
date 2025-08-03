 
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
                print(f"Deposited: ${amount}")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 2:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount}")
                else:
                    print("Insufficient funds.")
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 3:
            account.display_balance()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
