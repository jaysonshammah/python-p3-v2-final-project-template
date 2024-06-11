from helpers import (
    exit_program,
    add_client,
    view_clients,
    update_client,
    delete_client,
    add_account,
    view_accounts,
    update_account,
    delete_account,
    add_asset,
    view_assets,
    update_asset,
    delete_asset,
    add_holding,
    view_holdings,
    update_holding,
    delete_holding
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye")
            exit_program()
        elif choice == "1":
            client_menu()
        elif choice == "2":
            account_menu()
        elif choice == "3":
            asset_menu()
        elif choice == "4":
            holding_menu()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Clients")
    print("2. Accounts")
    print("3. Assets")
    print("4. Holdings")


def client_menu():
    while True:
        print("\nCLIENT MENU:")
        print("1. Add a client")
        print("2. View all clients")
        print("3. Update a client")
        print("4. Delete a client")
        print("0. Back to main menu")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_client()
        elif choice == "2":
            view_clients()
        elif choice == "3":
            update_client()
        elif choice == "4":
            delete_client()
        else:
            print("Invalid choice")


def account_menu():
    while True:
        print("\nACCOUNT MENU:")
        print("1. Add an account")
        print("2. View all accounts")
        print("3. Update an account")
        print("4. Delete an account")
        print("0. Back to main menu")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            update_account()
        elif choice == "4":
            delete_account()
        else:
            print("Invalid choice")


def asset_menu():
    while True:
        print("\nASSET MENU:")
        print("1. Add an asset")
        print("2. View all assets")
        print("3. Update an asset")
        print("4. Delete an asset")
        print("0. Back to main menu")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_asset()
        elif choice == "2":
            view_assets()
        elif choice == "3":
            update_asset()
        elif choice == "4":
            delete_asset()
        else:
            print("Invalid choice")


def holding_menu():
    while True:
        print("\nHOLDING MENU:")
        print("1. Add a holding")
        print("2. View all holdings")
        print("3. Update a holding")
        print("4. Delete a holding")
        print("0. Back to main menu")
        choice = input("> ")
        if choice == "0":
            break
        elif choice == "1":
            add_holding()
        elif choice == "2":
            view_holdings()
        elif choice == "3":
            update_holding()
        elif choice == "4":
            delete_holding()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
