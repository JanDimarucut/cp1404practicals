total = 0

number_of_item = int(input("Enter number of items: "))

while number_of_item <= 0:
    print("Invalid number of items!")
    number_of_item = int(input("Enter number of items: "))

for i in range(number_of_item):
    price = float(input("Item price: "))
    total += price

if total > 100:
    total_price = total - 0.1
else:
    total_price = total

print("Total price for {} item is ${:.2f}".format(number_of_item, total_price))


#Incomplete, the 10% does not work