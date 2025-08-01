import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    try:
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        if amount.is_integer():
            print(f"Deposited: ${int(amount)}")
        else:
            print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            if amount.is_integer():
                print(f"Withdrew: ${int(amount)}")
            else:
                print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()