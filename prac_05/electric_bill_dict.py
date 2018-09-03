
tariff_dict = {"TARIFF 11": 0.244618, "TARIFF 31": 0.136928, "TARIFF 15": 0.437952, "TARIFF 16": 0.482019,
               "TARIFF 17": 0.294025}

for key in tariff_dict:
    print(key)

user_choice = input("Select a tariff: ").upper()

while user_choice != "":
    if user_choice in tariff_dict:
        print(tariff_dict[user_choice])

        daily_use = float(input("Enter daily use in kWh: "))
        number_billing_days = int(input("Enter number of billing days: "))
        estimated_bill = (tariff_dict[user_choice] * daily_use) * number_billing_days
        print("Estimated bill: ${}".format(estimated_bill))

    else:
        print("Invalid input")
    user_choice = input("Select a tariff: ").upper()

print("Farewell")