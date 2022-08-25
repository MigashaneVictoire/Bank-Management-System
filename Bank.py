from os.path import exists as file_exists
import BugSolutions as FIX
import pandas as pd
import openpyxl
import datetime
import random
import time
import re

FIX = FIX.CustomFix()

# Read the client
excelFile = "Banking User Info.xlsx"
file = pd.read_excel(excelFile)


class Client:
    # get first name
    def get_firstName(self):
        first_name = input("Enter your first name ex:(Alex) \n")
        return FIX.re_match_name(first_name)

    # get last name
    def get_lastName(self):
        last_name = input("Enter your last name ex:(Monroe) \n")
        return FIX.re_match_name(last_name)

    # get user email
    def get_email(self):
        email = input("Enter your email address: \n")
        return FIX.validate_email(email)

    # get user phone number
    def get_phone(self):
        try:
            phone = int(input("Enter your phone number: \n"))
            if len(str(phone)) < 10 or len(str(phone)) > 10:
                print("Phone number must be of length 10")
                return Client().get_phone()
            else:
                return phone
        except ValueError:
            print("Phone number must contain only digits..")
            return Client().get_phone()

    # get user address
    def get_address(self):
        try:
            print("What is your address?")
            streetNO = FIX.get_street_num()
            streetName = FIX.get_street_name()
            cityName = FIX.get_city_name()
            state = FIX.get_state_name()
            zipcode = FIX.get_zipcode()
            country = "USA"

            # used only to populate the excel file
            # streetNO = random.randint(1,9999)
            # streetName = random.choice(FIX.auto_fill_client_street())
            # cityName = random.choice(FIX.auto_fill_client_city())
            # state = "Florida"
            # zipcode = random.choice(FIX.auto_generate_zipcode())
            # country = "USA"
            address = f"{streetNO} {streetName}, {cityName}, {state} {zipcode}, {country}"
            return address
        except ValueError:
            print("Your input does not meet address requirements...\nPlease Try again!")
            return Client().get_address()

    # get account type
    def get_accType(self):
        accType = input("Is this a Checking(C) or saving(S) account?\n")
        if accType == "C" or accType == "c":
            return "checking"
        elif accType == "S" or accType == "s":
            return "saving"
        else:
            print("Not a valid option")
            return Client().get_accType()

    # create a new account
    def createAcc(self):
        accNO = random.randint(pow(10, 9), pow(99, 5))
        routNO = random.randint(pow(10, 10), pow(99, 6))

        # used when creatinga real account
        date = datetime.datetime.now()
        _first_name = Client().get_firstName()
        _last_name = Client().get_lastName()
        _accType = Client().get_accType()
        _phone = Client().get_phone()
        _email = Client().get_email()
        _address = Client().get_address()
        _balance = 0

        # used only to populate the excel file
        # _start = datetime.datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
        # _endTime = datetime.datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
        # date = FIX.random_date(_start, _endTime)
        #
        # _first_name = random.choice(FIX.auto_fill_client_names())
        # _last_name = random.choice(FIX.auto_fill_client_names())
        # _accType = random.choice(["Saving", "Checking"])
        # _phone = random.randint(1234567890,9999999999)
        # _email = f"{_last_name}{_first_name}@{random.choice(['gmail','yahoo'])}.com"
        # _address = Account().get_address()
        # _balance = random.randint(0,500000)

        Client().saveAcc(date, accNO, routNO, _accType, _first_name, _last_name, _phone, _email, _address, _balance)

        print(
            f"Congratulation {_last_name}, your {_accType} account has been created!\n")

        return {"Account Number": accNO, "Account type": _accType}

    # def debitCard(self):
    #     debitCode = 4498
    #     _card = f"{debitCode}{random.randint(111111111111, 999999999999)}"
    #     return int(_card)

    # def Add_column(self):
    #     if file["Account Type"] == "Checking":
    #         file["Debit Card"] = Account().debitCard()
    #     else:
    #         file["Debit Card"] = None
    #     file.save(excelFile)

    # save created accounts to excel file
    def saveAcc(self, date_joined, accNO, routNO, accType, first_name, last_name, phoneNO, user_email, user_address,
                balance):
        groupID = "None"
        accounts = {"Date": date_joined,
                    "Account NO": accNO,
                    "Routing NO": routNO,
                    "Account Type": accType,
                    "First Name": first_name,
                    "Last Name": last_name,
                    "Balance": balance,
                    "Phone": phoneNO,
                    "Email": user_email,
                    "Address": user_address,
                    "GroupID": groupID}

        accounts = pd.DataFrame(accounts, index=[True])
        if file_exists(excelFile):
            # appending the data to the excel file
            with pd.ExcelWriter(excelFile, mode="a", engine="openpyxl",
                                if_sheet_exists="overlay") as writer:
                accounts.to_excel(writer, sheet_name="Sheet1", header=None, startrow=writer.sheets["Sheet1"].max_row,
                                  index=[True])
        else:
            # create a new file
            return accounts.to_excel(excelFile)

    def showAcc(self):
        _first_name = FIX.re_match_name(input("Enter account holder first name:\n"))
        _last_name = FIX.re_match_name(input("Enter account holder last name:\n"))
        client_info = file.loc[(file["First Name"] == _first_name) & (file["Last Name"] == _last_name)]
        return f"First Name: {_first_name} \nLast Name: {_last_name} \nAccount Number: {list(client_info['Account NO'])[0]}" \
               f" \nAccount Type: {list(client_info['Account Type'])[0]} \nBalance: ${list(client_info['Balance'])[0]} "


    def remove_client(self):
        try:
            print("Warning: This action will remove your account from our database... Do you wish to continue?")
            resp = input("Yes or No: \n")
            if resp == "No":
                return "We are glad to have you with us!"
            elif resp == "Yes":
                _accNo = int(input("Enter your account number to proceed: \n"))
                acc_location = FIX.get_cell_coordinate_by_UNIQUE_value(_accNo)
                FIX.remove_account(int(acc_location[1]))
                return "Sorry to see you go... Your account has been removed"
            else:
                print("Please reply with 'Yes' or 'No'!")
                return Client().remove_client()
        except IndexError:
            print("The account associated with this number was not found!")
            return Client().remove_client()
        except ValueError:
            print("You must number a valid account number!")
            return Client().remove_client()





    # get account balance
    def get_accBalance(self):
        try:
            _first_name = input("Enter account holder first name: \n")
            _last_name = input("Enter account holder last name: \n")
            # locate user by last name from excel
            _accBalance = list(file.loc[(file["First Name"] == _first_name) & (file["Last Name"] == _last_name)]["Balance"])
            return f"Your account balance is ${_accBalance[0]}"
        except FileNotFoundError:
            return FileNotFoundError
        except IndexError:
            print("The name you entered was not found! \nPlease try again!")
            return Client().get_accBalance()

    def accDeposit(self):
        try:
            _first_name = input("Enter account holder first name:\n")
            _last_name = input("Enter account holder last name: \n")
            _deposit_amount = int(input("Enter deposit amount: \n"))

            _acc_balance = list(file.loc[(file["First Name"] == _first_name) & (file["Last Name"] == _last_name)]["Balance"])

            _acc_NewBalance = _acc_balance[0] + _deposit_amount

            _cell_address = FIX.get_cell_coordinate_by_TWO_values(_acc_balance[0], _first_name, _last_name)
            FIX.change_excel_cell_value(_cell_address, _acc_NewBalance)

            return f"You have deposited ${_deposit_amount} into {_last_name}'s account...\n " \
                   f"Your new account balance is ${_acc_NewBalance}... Have greate day! "
        except FileNotFoundError:
            return FileNotFoundError
        except IndexError:
            print("The name you entered was not found! \nPlease try again!")
            return Client().accDeposit()
        except ValueError:
            print("You entered a invalid number! \nPlease try again!")
            return Client().accDeposit()

    def accWithdraw(self):
        try:
            _first_name = input("Enter account holder first name:\n")
            _last_name = input("Enter account holder last name: \n")
            _withdraw_amount = int(input("Enter withdraw amount: \n"))

            _acc_balance = list(
                file.loc[(file["First Name"] == _first_name) & (file["Last Name"] == _last_name)]["Balance"])

            _acc_NewBalance = _acc_balance[0] - _withdraw_amount

            if _acc_NewBalance < 0:
                return "Not enough funds in your account!"
            else:
                _cell_address = FIX.get_cell_coordinate_by_TWO_values(_acc_balance[0], _first_name, _last_name)
                FIX.change_excel_cell_value(_cell_address, _acc_NewBalance)

                return f"You have withdrawn ${_withdraw_amount} from {_last_name}'s account...\n " \
                       f"Your new account balance is ${_acc_NewBalance}... Have greate day!"
        except FileNotFoundError:
            return FileNotFoundError
        except IndexError:
            print("The name you entered was not found! \nPlease try again!")
            return Client().accWithdraw()
        except ValueError:
            print("You entered a invalid number! \nPlease try again!")
            return Client().accWithdraw()
