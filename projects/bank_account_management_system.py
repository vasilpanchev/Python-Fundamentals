# 🏦 Enhanced Bank Account Management System

# Data Structures to Store Information
account_holders = []  # Account names
balances = []  # Account balances
transaction_histories = []  # Account transaction logs
loans = []  # Account loan details

MAX_LOAN_AMOUNT = 10_000
INTEREST_RATE = 0.03


def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to Enhanced Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")


def create_account(account_name=""):
    """Create a new account."""
    if account_name == "":
        account_name = input("Enter account name: ")
    account_holders.append(account_name)
    balances.append(0)
    loans.append(0)
    print("✅ Account created successfully.")


def deposit():
    """Deposit money into an account."""
    account_name = input("Enter account name to deposit to: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                deposit()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                deposit()

    sum_to_deposit = float(input("Enter a sum to deposit: "))
    balances[account_index] += sum_to_deposit
    transaction_histories.append(f"{account_name} -> deposited ${sum_to_deposit}")
    print("✅ Balance deposited successfully.")


def withdraw():
    """Withdraw money from an account."""
    account_name = input("Enter account name to withdraw from: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                withdraw()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                withdraw()
    while True:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if balances[account_index] >= withdraw_amount:
            balances[account_index] -= withdraw_amount
            print(f"✅ Successfully withdrew {withdraw_amount}.")
            transaction_histories.append(f"{account_name} -> withdrew ${withdraw_amount}")
            break
        else:
            print(f"Withdrawal amount ${withdraw_amount} is more than balance.\nTry again.")


def check_balance():
    """Check balance of an account."""
    account_name = input("Enter account name to check balance of: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                check_balance()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                check_balance()

    print(f"💵 {account_name}'s balance: ${balances[account_index]}")


def list_accounts():
    """List all account holders and details."""
    for i in range(len(account_holders)):
        print(f"Account holder:{account_holders[i]} -> Balance: ${balances[i]}")


def transfer_funds():
    """Transfer funds between two accounts."""
    account1_name = input("Enter account name to transfer from: ")
    account2_name = input("Enter account name to transfer to: ")
    amount = float(input("Enter amount to transfer"))

    account1_index = None
    account2_index = None
    is_found1 = False
    is_found2 = False

    while account1_index is None and account2_index is None:
        if (account1_name and account2_name) in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account1_name:
                    account1_index = i
                    is_found1 = True
                    if is_found2 is True:
                        break
                elif account_holders[i] == account2_name:
                    account2_index = i
                    is_found2 = True
                    if is_found1 is True:
                        break

        else:
            print("❌ Accounts with those names do not exist.")

    if balances[account1_index] < amount:
        print(f"{account1_name} has less than ${amount} to transfer in their account.")
    balances[account1_index] -= amount
    balances[account2_index] += amount

    transaction_histories.append(f"✅ {account1_name} -> transferred ${amount} to {account2_name}.")


def view_transaction_history():
    """View transactions for an account."""
    account_name = input("Enter account name to check transaction history of: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                view_transaction_history()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                view_transaction_history()

    print(f"{account_name}'s transaction history:")
    for i in range(len(transaction_histories)):
        transaction_name, transaction = transaction_histories[i].split(' -> ')
        if transaction_name == account_name:
            print(f"- {transaction}")


def apply_for_loan():
    """Allow user to apply for a loan."""
    account_name = input("Enter account name to apply for loan for: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                apply_for_loan()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                apply_for_loan()

    loan_amount = float(input())
    if loan_amount > MAX_LOAN_AMOUNT:
        print(f"The amount you want to loan is larger than {MAX_LOAN_AMOUNT}.")
        exit()
    loans[account_index] = loan_amount + INTEREST_RATE * loan_amount
    print(f"✅ Successfully loaned ${loan_amount}. Amount to repay: ${loans[account_index]}")


def repay_loan():
    """Allow user to repay a loan."""
    account_name = input("Enter account name to apply for loan for: ")
    account_index = None
    while account_index is None:
        if account_name in account_holders:
            for i in range(len(account_holders)):
                if account_holders[i] == account_name:
                    account_index = i
                    break
        else:
            print("❌ Account with this name does not exist.")
            input("1️⃣ Press 1 to retry with a new name.")
            input("2️⃣ Press 2 to create a new account with this name.")
            choice = int(input("Enter your choice: "))
            # Map choices to functions
            if choice == 1:
                repay_loan()
            elif choice == 2:
                create_account(account_name)
            else:
                print("❌ Invalid choice.")
                repay_loan()

    if balances[account_index] < loans[account_index]:
        print(f"The amount you want to repay is larger than your balance (Balance: ${balances[account_index]}).")
        exit()
    print(f"✅ Successfully repayed your loan ${loans[account_index]}.")
    loans[account_index] = 0


def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic


def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again!")


if __name__ == "__main__":
    main()
