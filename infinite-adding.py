# Infinite Adding
# For exploring infinite series

coefficient = 1
fraction = 0.5
iteration = 10
total = fraction
exponent = fraction

for i in range(0, iteration):
    print(total)
    exponent *= fraction
    total += exponent
