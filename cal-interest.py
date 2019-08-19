def main():
    print("***********************************")
    print("______ _       _____       _      ")
    print("|  ___(_)     /  __ \     | |     ")
    print("| |_   _ _ __ | /  \/ __ _| | ___ ")
    print("|  _| | | '_ \| |    / _` | |/ __|")
    print("| |   | | | | | \__/\ (_| | | (__ ")
    print("\_|   |_|_| |_|\____/\__,_|_|\___|")
    print("***********************************")
    print("***********************************")
    print("********Welcome to FinCalc*********\n")
    select()

def select():
    print("Please select what to do by typing the number...\n")
    print("1 - simple annual interest")
    print("2 - payments in advance")
    print("3 - payments in arear")
    print("4 - effective interest rate")

    argument = input("selection: ")

    if argument == "1": interest()
    elif argument == "2": payments_ad()
    elif argument == "3":payments_ar()
    elif argument == "4":eff_interest()
    else: print("invalid selection, try again...")
    select()

def interest():
    print("Enter the Amount of years")
    years = int(input("...yrs "))

    print("Enter the capital at the beginning")
    start_balance = float(input("... "))

    print("Enter the monthly investment")
    monthly_invest = float(input("... "))

    print("Enter the yearly interest rate")
    interest = float(input("...% "))/100

    print("********************************")

    monthly_invest = monthly_invest * 12
    end_balance = 0
    total_invest = 0
    total_interest = 0

    for i in range(0, years):
        if end_balance == 0:
            end_balance = start_balance


        end_balance = (end_balance + monthly_invest) * (1 + interest)
        total_invest = (monthly_invest * years)
        total_interest = (end_balance - (total_invest + start_balance))


    print("After " f'{years}' " years, the final capital would be " f'{end_balance}')
    print("of which the total amount of investments would be " f'{total_invest}' ", interest amount would be " f'{total_interest}')

def payments_ad():
    print("test1")

def payments_ar():
    print("test2")

def eff_interest():
    print("test3")

select()
