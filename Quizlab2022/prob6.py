#Problem6 Final labquiz2022

account = {}
#open bank account
while True:
    inp = input("Open bank account with initial amount (account number, amount): ")
    if inp == "done":
        break
    acnum, inam = inp.split()
    acnum, inam = int(acnum),int(inam)
    if acnum not in account:
        account[acnum] = inam
def deposit(acnum, amount):
    account[acnum] += amount
    print("Available amount of acoount number %d is %.2f."%(acnum,account[acnum]))

def withdraw(acnum, amount):
    if account[acnum] > amount: #When our balance is more than the amount we want to withdraw
        account[acnum] -= amount
        print("Available amount of account number %d is %.2f."%(acnum,account[acnum]))
    else: #When our balance isn't enough to withdraw
        print("You don't have enough amount.")
        print("Available amount of account number %d is %.2f."%(acnum,account[acnum]))

#Transaction
while True:
    inp = input("Enter transaction (account number, withdrawal/deposit, amount): ")
    if inp == "done":
        break
    acnum,tran,amount = inp.split()
    acnum, amount = int(acnum),int(amount)
    if acnum in account:
        if tran == "d":
            deposit(acnum,amount)
        elif tran == "w":
            withdraw(acnum, amount)
    else:
        print("Invalid account, Please enter transaction again.")
        
        
        

# Solution without defining funtions
account = {}
#open bank account
while True:
    inp = input("Open bank account with initial amount (account number, amount): ")
    if inp == "done":
        break
    acnum, inam = inp.split()
    acnum, inam = int(acnum),int(inam)
    if acnum not in account:
        account[acnum] = inam
#Transaction
while True:
    inp = input("Enter transaction (account number, withdrawal/deposit, amount): ")
    if inp == "done":
        break
    acnum,tran,amount = inp.split()
    acnum, amount = int(acnum),int(amount)
    if acnum in account:
        if tran == "d":
            account[acnum] += amount
            print("Available amount of account number %d is %.2f."%(acnum,account[acnum]))
        elif tran == "w":
            if account[acnum] > amount: #When our balance is more than the amount we want to withdraw
                account[acnum] -= amount
                print("Available amount of account number %d is %.2f."%(acnum,account[acnum]))
            else: #When our balance isn't enough to withdraw
                print("You don't have enough amount.")
                print("Available amount of account number %d is %.2f."%(acnum,account[acnum]))
    else:
        print("Invalid account, Please enter transaction again.")