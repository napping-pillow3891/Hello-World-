#input
kwh = int(input("Enter the KW hours used: "))
#rates
rateFirst = 0.07633
rateOver = 0.09259

#caculations
if kwh <= 1000:
    amount = kwh * rateFirst
else:
    amount = (1000 * rateFirst) + ((kwh - 1000) * rateOver)

print(f"Amount owed is ${amount}")
