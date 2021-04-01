# Infinite Adder
# For calculating infinite series
from fractions import Fraction as frac

# Initial fraction to be added to powers of itself
fraction = frac(1, 2)
# Entire series is multiplied by `coefficient`
coefficient = frac(1, 2)
# How far into the series to add
iterations = 10

# Loop handling variables
exponent = fraction
total = coefficient*fraction

for i in range(0, iterations):
    print(str(total)+'='+str(float(total)))
    exponent *= fraction
    total += coefficient*exponent
