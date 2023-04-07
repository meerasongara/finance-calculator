import math

print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#input for the type 
choice = input()

#if the user selects investment
if  choice == 'investment' or choice == "INVESTMENT" or choice == 'Investment':
#input the values
    presentvalue = int(input("Enter deposit amount: "))
    rateofinterest = int(input("Enter the rate of interest as a percentage: "))
    time = int(input("Enter the number of years: "))
    type_interest = input("Enter the type of interest:\ncompound\nsimple\n")
#select the type of interest
    if type_interest == "simple":
        A = presentvalue * (1 + rateofinterest*time)
    elif type_interest == "compound":
         A = presentvalue * math.pow((1 + rateofinterest), time)
    else:
        print("Type of interest is invalid.")

    print("The amount after", time, "years is", round(A,2))

#if user selects bond
elif choice == 'bond' or choice == "BOND" or choice == 'Bond':
#input the values
    presentvalue = int(input("Enter the present value of the house: "))
    rateofinterest = float(input("Enter the rate of interest: "))
    numofmonths = int(input("Enter the number of months for the bond: "))
    i = numofmonths/12

    repayment = (i * presentvalue)/(1 - (1 + i)**(-numofmonths))

    print("The repayment after", numofmonths, "months is", round(repayment,2))

else:
    print("This choice is invalid.")