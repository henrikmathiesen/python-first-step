#
# Input

print("Enter name")
name = input()

print("Enter EPS")
eps = input()

print("Enter growth rate")
gr = input()

print("Enter current PPS")
pps = input()

#
# Constants

noGrPe = 0.085
rrOfR = 0.03

#
# Convert input

eps = float(eps)
gr = float(gr)
gr = gr / 100
pps = float(pps)

#
# Calculate

iv = (eps * (noGrPe + (2 * gr)) * 4.4) / rrOfR
diff = iv / pps

#
# Convert result

iv = round(iv)
iv = str(iv)
pps = str(pps)
diff = str(diff)

#
# Print result

print(name + " >> " + "PPS: " + pps + " | IV: ~" + iv + " | DIFF: " + diff)
