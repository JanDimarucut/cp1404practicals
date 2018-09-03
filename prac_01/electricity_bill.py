TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


print("Electricity bill estimator")
price_per_kWh = int(input("Enter cents per kWh: "))
convert_cents = price_per_kWh / 100

daily_use_kWh = float(input("Enter daily use in kWh: "))

billing_period = int(input("Enter number of billing days: "))

estimated_bill = (convert_cents * daily_use_kWh) * billing_period
print("Estimated bill: ${}".format(estimated_bill))

#2
print("Electricity bill estimator 2.0")

tariff = input("Which tariff? 11 or 31: ")
if tariff == "11":
    daily_use_kWh = float(input("Enter daily use in kWh: "))
    number_billing_days = int(input("Enter number of billing days: "))
    estimated_bill = (TARIFF_11 * daily_use_kWh) * number_billing_days
    print("Estimated bill: ${}".format(estimated_bill))

elif tariff == "31":
    daily_use_kWh = int(input("Enter daily use in kWh: "))
    number_billing_days = float(input("Enter number of billing days: "))
    estimated_bill = (TARIFF_31 * daily_use_kWh) * number_billing_days
    print("Estimated bill: ${}".format(estimated_bill))

else:
    print("Invalid")