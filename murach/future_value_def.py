#!/usr/bin/env python3

import validation as v

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

def main():
    choice = "Y"
    while choice.upper() == "Y":
        # get input from the user
        monthly_investment = v.get_float("Enter monthly investment:\t", 0, 10000)
        yearly_interest_rate = v.get_float("Enter yearly interest rate:\t", 0, 15)
        years = v.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(monthly_investment, yearly_interest_rate, years)

        print(f"\nFuture value:\t\t\t{round(future_value, 2)}\n")

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("¡Adios!")
    
if __name__ == "__main__":
    main()
