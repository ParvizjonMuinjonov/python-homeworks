def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount *= (1 + rate)
        print(f"Year {year}: $ {amount:.2f}")


initial_amount = float(input("Enter your initial deposit: "))
annual_rate = float(input("Enter your fixed percentage: "))
num_years = int(input("Enter the number of years: "))

invest(initial_amount, annual_rate, num_years)