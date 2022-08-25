# import PairAcc # expention has been temporatity suspended
from tkinter import messagebox
import os
import Bank

class DMS:

    def _main_menu(self):
        print("  ┌───────────────────────────────────────────────┐  ")
        print("  |    ╭┼┼╮    ||    II  ||\  /||  ||``|   /\     |  ")
        print("  |    ╰┼┼╮    ||    ||  || \/ ||  ||<<   //\\\    |  ")
        print("  |    ╰┼┼╯    ||III ||  ||    ||  ||,,| //──\\\   |  ")
        print("  |     ──────────────── *$* ────────────────     |  ")
        print("  |  ╭───────────────────╮ ╭───────────────────╮  |  ")
        print("  |  | 1 ► Account       | | 2 ► Transactions  |  |  ")
        print("  |  ╰───────────────────╯ ╰───────────────────╯  |  ")
        print("  |  ╭───────────────────╮ ╭───────────────────╮  |  ")
        print("  |  | 3 ► Group         | | 4 ► Help          |  |  ")
        print("  |  ╰───────────────────╯ ╰───────────────────╯  |  ")
        print("  |      ║│┃┃║║│┃║│║┃│   *$*   ║│┃┃║║│┃║│║┃│      |  ")
        print("  └───────────────────────────────────────────────┘  ")
        try:
            _user_choice = int(input("How can I help you today: \n"))
            if _user_choice == 1:
                DMS()._acc_manu()
            elif _user_choice == 2:
                DMS()._trans_menu()
            elif _user_choice == 3:
                print("This option is not active at this time...!")
                return DMS()._trans_menu()
            elif _user_choice == 4:
                return "Please refer to the readme.txt file for this project."
            else:
                print("Invalid option... Please try again!")
                DMS()._main_menu()
        except ValueError:
            print("Invalid option... Please try again!")
            DMS()._main_menu()

    def _acc_manu(self):
        print("  ┌──────────────────────────────┐  ")
        print("  |             ╭┼┼╮             |  ")
        print("  |             ╰┼┼╮             |  ")
        print("  |             ╰┼┼╯             |  ")
        print("  |            Account           |  ")
        print("  |        ───── *$* ─────       |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 1 ► Create Account     |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 2 ► Get Account Info   |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 3 ► Remove Account     |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 4 ► Main Manu          |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |        ║│┃┃║║│┃║│║┃│         |  ")
        print("  └──────────────────────────────┘  ")

        try:
            _user_choice = int(input("Welcome to Account, what would you like to do?\n "))
            if _user_choice == 1:
                Bank_user.createAcc()
            elif _user_choice == 2:
                print(Bank_user.showAcc())
            elif _user_choice == 3:
                print(Bank_user.remove_client())
            elif _user_choice == 4:
                DMS()._main_menu()
            else:
                print("Invalid option... Please try again!")
                DMS()._acc_manu()
        except ValueError:
            print("Invalid option... Please try again!")
            DMS()._trans_menu()

    def _trans_menu(self):
        print("  ┌──────────────────────────────┐  ")
        print("  |             ╭┼┼╮             |  ")
        print("  |             ╰┼┼╮             |  ")
        print("  |             ╰┼┼╯             |  ")
        print("  |          Transactions        |  ")
        print("  |        ───── *$* ─────       |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 1 ► View Balance       |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 2 ► Deposit            |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 3 ► Withdraw           |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |  ╭────────────────────────╮  |  ")
        print("  |  | 4 ► Main Manu          |  |  ")
        print("  |  ╰────────────────────────╯  |  ")
        print("  |        ║│┃┃║║│┃║│║┃│         |  ")
        print("  └──────────────────────────────┘  ")

        try:
            _user_choice = int(input("Welcome to Transactions, what would you like to do?\n "))
            if _user_choice == 1:
                print(Bank_user.get_accBalance())
            elif _user_choice == 2:
                print(Bank_user.accDeposit())
            elif _user_choice == 3:
                print(Bank_user.accWithdraw())
            elif _user_choice == 4:
                DMS()._main_menu()
            else:
                print("Invalid option... Please try again!")
                DMS()._trans_menu()
        except ValueError:
            print("Invalid option... Please try again!")
            DMS()._trans_menu()

if __name__ == "__main__":
    DMS_user = DMS()
    Bank_user = Bank.Client()
    print(DMS_user._main_menu())
