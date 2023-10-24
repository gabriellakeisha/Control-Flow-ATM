#creating PIN and balance for the account
balance = 10000
pin = "1207"

#input the PIN
print ("Hello, welcome to Dev's ATM")
print ("Input your PIN")
input_pin = input ()

#if statement
if input_pin == "1207":
    print ("Your account balance is $" + str (balance))
    #asking for withdrawal
    print ("Would you like to withdraw/deposit money?")
    request = input ()
    #if statement for if user wants to withdraw money
    if request == "withdraw":
        print ("Enter the amount:")
        amount = int(input ())
        new_balance = balance-amount 
        print ("Thank you for the transaction. Now, your account balance is $" + str (new_balance))
    elif request == "deposit":
        print ("Enter the amount:")
        amount = int(input())
        new_balance2 = balance+amount
        print ("Thank you for the transaction. Now, your account balance is $" + str (new_balance2))
    else:
        print ("No transaction for today. Thank you")
else: 
    print ("Your PIN is incorret, try again")


