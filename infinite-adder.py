# Infinite Adder
# For calculating infinite series
import argparse
from fractions import Fraction as frac

# Handle command line arguments
parser = argparse.ArgumentParser()

parser.add_argument('fraction', nargs='?', default='1/2', 
        help='fraction to add powers of. default is 1/2')
parser.add_argument('coefficient', nargs='?', default='1', 
        help='coefficient to multiply entire series by. default is 1')
parser.add_argument('-i', '--iterations', type=int, default=10, 
        help='set the number of iterations. default is 10')

args = parser.parse_args()

# Convert inputs from string to fraction
fraction = frac(args.fraction)
coefficient = frac(args.coefficient)

# Variables for looping
exponent = fraction
total = coefficient*fraction

for i in range(0, args.iterations):
    print(str(total)+'='+str(float(total)))
    exponent *= fraction
    total += coefficient*exponent
