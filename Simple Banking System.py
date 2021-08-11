Amount=1234
pin=4444

# Case withdrawl Function
def caseWithdrawl():
    global pin
    global Amount
    PIN=int(input('Enter PIN to proceed: '))
    if(PIN==pin):
        amt=int(input("Enter Amount that you wish to Withdrawl : "))
        if(amt<Amount):
            Amount-=amt
            print(f"{amt} withdrawl Successfully!!!")
        else:
            print("you don't have that much Amount")
    else:
        print("___________________________", end="\n")
        print("\nYou Have Entered Invalid PIN")


# Case credit Function
def caseCredit():
    global pin
    global Amount
    PIN=int(input('Enter PIN to proceed: '))
    if(PIN==pin):
        amt=int(input("Enter Amount that you wish to Credit : "))
        Amount+=amt
        print(f"{amt} Credit Successfully!!!")
    else:
        print("___________________________", end="\n")
        print("\nYou Have Entered Invalid PIN")



# change PIN Function
def changePIN():
    global pin
    PIN=int(input('Enter old PIN to proceed: '))
    if(PIN==pin):
        newPIN = int(input("Enter new PIN :"))
        pin = newPIN
        print("PIN updated Successfully!!!")
    else:
        print("___________________________", end="\n")
        print("\nYou Have Entered Invalid PIN")



# Code Started From here
print("Welcome to Capital Bank", end="\n")
print("___________________________", end="\n")
while(1):
    print("Choose from below options", end="\n")
    print('''
1. Case withdrawal        2. Case credit
3. Change password        4. Show Amount
5. Exit ''')
    opt=int(input("Enter your option : "))
    if(opt==1):
        caseWithdrawl()
    if(opt==2):
        caseCredit()
    if(opt==3):
        changePIN()
    if(opt==4):
        print(f'''
        ------------
          {Amount}
        ------------
        ''')
        
    if(opt==5):
        break
    print("\n")



