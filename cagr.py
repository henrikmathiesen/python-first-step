#
# Input

print("Enter beginning value:")
bValue = input()

print("Enter ending value:")
eValue = input()

print("Enter number of periods:")
periods = input()

#
# Convert input

bValue = float(bValue)
eValue = float(eValue)
periods = int(periods)

#
# Calculate

cagr = ( (eValue / bValue) ** (1/periods) ) - 1

#
# Convert result

cagr = cagr * 100
cagr = round(cagr)
cagr = str(cagr)

#
# Print result

print("CAGR: " + cagr + "%")


