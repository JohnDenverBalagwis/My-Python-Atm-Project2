AppRunning = True
while AppRunning == True:
    print("===================================================")
    print(" WELCOME TO BALAGWIS ATM SYSTEM")
    print("===================================================")
    operation = str(input("Choose Operation: \n[1] Balance \n[2] Withdraw\n[3] Deposit \n[4] Exit \n\nOperation: "))

    if operation == '1':
        username = input("Username: ")
        pin = input("Pin Number: ")
        file = username + pin
        print(file)
        try:
            with open("accounts/"+file+".txt", "r") as account:
                amount = account.readline()
                print("===================================================")
                print("Your balance is Php {:.2f}".format(float(amount)))
                print("===================================================")
        except FileNotFoundError:
            print("============================================================")
            print("Operation Error: Either username or pin number is incorrect.")
            print("============================================================")

    elif operation == '2':
        username = input("Username: ")
        pin = input("Pin Number: ")
        file = username + pin
        print(file)
        try:
            account = open("accounts/"+file+".txt", "r")
            amount = account.readline()
            account.close()
            withdraw = input("Amount to withdraw: ")
            if float(amount) > float(withdraw):
                newBalance = float(amount) - float(withdraw)
                print("===================================================")
                print("Withdraw Success: Your new balance is Php {:.2f}".format(newBalance))
                print("===================================================")
                account = open("accounts/"+file+".txt", "w")
                newBalance = "{:.2f}".format(newBalance)
                account.truncate(0)
                account.writelines(str(newBalance))
                account.close()
            elif amount == withdraw:
                print("===================================================")
                print("Operation Error: You can't withdraw the whole amount.")
                print("===================================================")
            else:
                print("===================================================")
                print("Operation Error: Not enough balance.")
                print("===================================================")
        except FileNotFoundError:
            print("============================================================")
            print("Operation Error: Either username or pin number is incorrect.")
            print("============================================================")

    elif operation == '3':
        username = input("Username: ")
        pin = input("Pin Number: ")
        file = username + pin
        print(file)
        try:
            account = open("accounts/"+file+".txt", "r")
            amount = account.readline()
            account.close()
            deposit = input("Amount to deposit: ")
            newBalance = float(amount) + float(deposit)
            print("===================================================")
            print("Deposit Success: Your new balance is Php {:.2f}".format(newBalance))
            print("===================================================")
            account = open("accounts/"+file+".txt", "w")
            newBalance = "{:.2f}".format(newBalance)
            account.truncate(0)
            account.writelines(str(newBalance))
            account.close()
        except FileNotFoundError:
            print("============================================================")
            print("Operation Error: Either username or pin number is incorrect.")
            print("============================================================")

    elif operation == '4':
        AppRunning = False



print("===================================================")
print("Thank you for using BALAGWIS ATM System.")
print("===================================================")