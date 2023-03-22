cb = 500.00
sb = 2000.00

print("Press \"q\" to quit, \"w\" to withdraw, \"t\" to transfer, and \"/bal\" to view balance.")
while True:
    query = input("Query: ")
    # quit
    if query == 'q':
        break
    
    # view balances
    if query == "/bal":
        print("Checking balance: $", format(cb, '.2f'))
        print("Savings balance: $", format(sb, '.2f'))
    
    # deposit to checking acc 
    if query == 'd':
        cb += float(input("Amount to deposit: "))
    
    # withdraw from checking acc
    if query == 'w':
        withdraw = float(input("Amount to withdraw: "))
        if withdraw <= cb:
            cb -= withdraw
        else:
            print("Insufficient funds")
            
    # transfer money from savings to checking acc
    if query == 't':
        transfer = float(input("Amount to transfer: "))
        if transfer <= sb:
            sb -= transfer
            cb += transfer
        else:
            print("Insufficient funds")
exit()
