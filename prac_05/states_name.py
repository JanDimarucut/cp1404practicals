
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

# 4

max_length = max(len(key) for key in STATE_NAMES)

for key in STATE_NAMES:
    print("{:{}} is {}".format(key, max_length, STATE_NAMES[key]))
