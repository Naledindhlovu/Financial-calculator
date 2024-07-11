#The user  should be allowed to choose which calculation they want to do.
#
# The first output that the user sees when the program runs should look like this :
import math
print( "************************************************************************************************")
print( "***********************************Finicial Calculator******************************************")
print( "************************************************************************************************")
print("--Bond to calculate the amount you'll have to pay on a home loan")
print("--Investment ti calculate the amount of interest you'll earn on interest.")
print( "************************************************************************************************")
    
def get_investment(choose):
    deposit = int(input('Enter the amount you will like to deposit: '))
    interest_rate = float(input('Enter the interest rate: '))
    period= int(input('Enter the period years of investing:  '))
    print('Choose Simple interest or compound interest')
    print('1- Simple interest')
    print('2- Compound interest')
    choice = int(input('Choice :'))
    r=interest_rate / 100
    P=deposit
    t=period

    while True: 
      if choice == 1:
        print( "****************SIMPLE INTEREST****************")
        A = P * (1 + r * t ) 
        total= round(A,2)
        print( f"Total Amount : R{total}")
        print( "********************************")
        calc()
      elif choice == 2:
        print( "****************COMPOUND INTEREST**************")
        A = P* math.pow((1+r),t)
        total= round(A,2)
        print( f"Total Amount : R{total}")
        print( "********************************")
        calc()
      else: 
        print('Invalid choice')
        print('1- Simple interest')
        print('2- Compound interest')
        choice = int(input('Choice :'))
def get_bond(choose):
    house_value= int(input("Enter Present value of the house: "))
    interest_rate = float(input('Enter the interest rate: '))
    period= int(input('Enter the period months to repay the bond:  '))
    n= period
    i=interest_rate/12001
              
    P = house_value
    x = (i*P)/1 - math.pow ((1+i),(-n))
    total = round(x,2)
    print( f"Monthly repayments : R{total}")
    print( "********************************")
    calc()

def calc():
    print("Choose between bond and investment ")
    print("1- Investment")
    print("2- Bond")
    print("3- EXIT")
    choose = int(input('Choice :'))
    while True:
        
        if choose == 1:
          print( "********************INVESTMENT******************")
          return get_investment(choose)
        
        elif choose == 2:
          print( "**********************BOND*********************")
          return get_bond(choose)
          
        elif choose == 3:
            print( "***************PROGRAM CLOSED******************")
            exit()
        else:
          print("Choose between bond and investment ")
          print("1- Investment")
          print("2- Bond")
          choose = int(input('Choice :'))

print(calc())
