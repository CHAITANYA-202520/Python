import logging as lg
lg.basicConfig(
    filename="app.log",
    level=lg.DEBUG,
    format="[%(asctime)s-%(levelname)s]-%(message)s"
)
# total Operations
operations =(
    "1. Balance\n",
    "2. withdraw\n",
    "3. deposit\n",
    "4. Transfer\n",
    "5. History\n",
    "6. Exit\n"
)
# account table
account_table={
    12345:6789,
    123456:6789
    }

#users_tables
users_table={
    12345:["Srinubabu","srinubabu@codegnan.com",1000],
    123456:["babu","gamil@com",2500]
    }


#transactions table

# Checking valid user
def valid_user(user_name:int,password:int):
    lg.debug("User in login page")
    if account_no in account_table:
        if account_table[user_name]==password:
            lg.info("User successfully logined")
            print("User successfully logined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check your login credentials")
        print("Please check your login credentials")
        return False

# balance function
def balance(user_name):
    lg.debug("User in balance page")
    if user_name in users_table:
        amount=users_table[user_name][2]
        lg.info(f"{user_name} user current balance is {amount}")
        print(f"{user_name} user current balance is {amount}")
    else:
        lg.warning("User not found")
        print("User not found")


# withdraw function
def withdraw(user_name):
    lg.debug("User in withdraw page")
    amount=users_table[user_name][2]
    withdraw_amount=int(input("Please enter withdraw amount:"))
    if amount>=withdraw_amount:
        users_table[user_name][2]-=withdraw_amount
        lg.info(f'{withdraw_amount} withdraw successful and current balance is {users_table[user_name][2]}')
        print(f'{withdraw_amount} withdraw successful and current balance is {users_table[user_name][2]}')

    else:
        lg.warning("Insufficient amount")
        print("Insufficient amount")
    

# deposit function
def deposit(user_name:int):
    lg.info("User in deposit page")
    deposit_amount=int(input("Please enter deposit amount:"))
    if user_name in users_table:
        users_table[user_name][2]+=deposit_amount
        lg.info(f'{deposit_amount} withdraw successful and current balance is {users_table[user_name][2]}')
        print(f'{deposit_amount} withdraw successful and current balance is {users_table[user_name][2]}')

    else:
        lg.warning("User not found")
        print("User not found")
    
    

# transfer function
def transfer(user_name):
    lg.debug("User in transfer page")
    receiver_account=int(input("Enter Receiver account number: "))
    amount=int(input("Enter amount: "))
    lg.info(f"receiver account is {receiver_account} and amount is {amount}")
    current_amount=users_table[user_name][2]
    if receiver_account in users_table:
        if current_amount>=amount:
            # amount updation in users table
            users_table[user_name][2]-=amount
            users_table[receiver_account][2]+=amount
            lg.info(f'{amount} transfer successfully and current balance is {users_table[user_name][2]}')
            print(f'{amount} transfer successfully and current balance is {users_table[user_name][2]}')

        else:
            lg.warning("Insufficient amount")
            print("Insufficient amount")
    else:
        lg.warning(f"{receiver_account} not found")
        print(f"{receiver_account} not found")

  

# history function
def history(user_name):
    lg.info("User in history page")
    print("History function under development process....")
  

# exit function
def exit_fun():
    lg.info("User in exit page")
    print("Successsfully exited, thank you for using codegnan online bank services")
    return True
    

#chose_operation function
def chose_operation(account_no,choice):
    lg.info("selected operation is {operations[choice-1]}")
    val= False
    if choice==1:
        balance(user_name=account_no)
    elif choice==2:
        withdraw(user_name=account_no)
    elif choice==3:
        deposit(user_name=account_no)
    elif choice==4:
        transfer(user_name=account_no)
    elif choice==5:
        history(user_name=account_no)
    elif choice==6:
        val = exit_fun()
    else:
        print("Please select between 1-6")
    if val:
        return val


if __name__=="__main__":
    print("Welcome to the online codegnan Banking")
    lg.info("Welcome to the online codegnan Banking")
    account_no=int(input("Please, enter account number: "))
    pin=int(input("Please enter pin number: "))
    lg.info(f"User credentials are {account_no} and {pin}")
    while True:
        if valid_user(user_name=account_no,password=pin):
            print(*operations)
            lg.info(operations)
            choice=int(input("Please select operation (1-6): "))
            exit_fun_val=chose_operation(account_no=account_no,choice=choice)
            if exit_fun_val:
                break
            
        else:
            lg.warning("User not found,please check with your login credentials")
            print("User not found,please check with your login credentials")
            break